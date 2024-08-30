import os
import requests
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

def fetch_combined_data(postcode):
    current_datetime = datetime.utcnow()
    fw48h_start = current_datetime.strftime("%Y-%m-%dT%H:%MZ")
    fw48h_url = f"https://api.carbonintensity.org.uk/regional/intensity/{fw48h_start}/fw48h/postcode/{postcode}"
    response = requests.get(fw48h_url)
    response.raise_for_status()
    data = response.json()
    return data['data']['data']

def create_text_tile(combined_renewable_perc, output_folder, timestamp):
    img = Image.new('RGBA', (640, 360), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Header Text
    header_font = ImageFont.truetype("arial.ttf", 24)
    draw.text((10, 10), "Manchester: M9 Postcode", fill="black", font=header_font)
    draw.text((10, 40), f"Wind & Solar: {combined_renewable_perc:.2f}%", fill="black", font=header_font)
    
    # Adding a 25-pixel space before the date and time
    y_position = 40 + 25 + 24  # 40 for initial Y, 25 for space, 24 for the header text height

    # Date and Time Text
    timestamp_font = ImageFont.truetype("arial.ttf", 35)
    date_time_text = timestamp.split("_")
    draw.text((10, y_position), date_time_text[0], fill="black", font=timestamp_font)
    draw.text((10, y_position + 50), date_time_text[1], fill="black", font=timestamp_font)
    
    img.save(os.path.join(output_folder, f"{timestamp}_transparent.png"))

def create_colored_tile(wind_perc, solar_perc, output_folder, timestamp):
    green_color = (0, 255, 0)
    grey_color = (211, 211, 211)
    combined_renewable_perc = wind_perc + solar_perc

    if combined_renewable_perc <= 30:
        color = grey_color
    else:
        factor = (combined_renewable_perc - 30) / 70  # Normalizing between 30% and 100%
        color = tuple(int(green_color[i] * factor + grey_color[i] * (1 - factor)) for i in range(3))
    
    img = Image.new('RGB', (640, 360), color)
    img.save(os.path.join(output_folder, f"{timestamp}_colored.png"))

def generate_excel(postcodes, base_output_folder):
    with pd.ExcelWriter(os.path.join(base_output_folder, "48_hour_forecast.xlsx"), engine='xlsxwriter') as writer:
        for postcode in postcodes:
            print(f"Fetching data for postcode: {postcode}")
            combined_data = fetch_combined_data(postcode)
            all_data = []

            for entry in combined_data:
                timestamp = datetime.strptime(entry['from'], "%Y-%m-%dT%H:%MZ").strftime("%Y-%m-%d %H:%M")
                row = {
                    "Timestamp": timestamp,
                    "Nuclear": next((item['perc'] for item in entry['generationmix'] if item['fuel'] == 'nuclear'), 0),
                    "Gas": next((item['perc'] for item in entry['generationmix'] if item['fuel'] == 'gas'), 0),
                    "Biomass": next((item['perc'] for item in entry['generationmix'] if item['fuel'] == 'biomass'), 0),
                    "Imports": next((item['perc'] for item in entry['generationmix'] if item['fuel'] == 'imports'), 0),
                    "Coal": next((item['perc'] for item in entry['generationmix'] if item['fuel'] == 'coal'), 0),
                    "Wind": next((item['perc'] for item in entry['generationmix'] if item['fuel'] == 'wind'), 0),
                    "Solar": next((item['perc'] for item in entry['generationmix'] if item['fuel'] == 'solar'), 0),
                    "Hydro": next((item['perc'] for item in entry['generationmix'] if item['fuel'] == 'hydro'), 0),
                    "Other": next((item['perc'] for item in entry['generationmix'] if item['fuel'] == 'other'), 0),
                    "Combined Wind & Solar": next((item['perc'] for item in entry['generationmix'] if item['fuel'] == 'wind'), 0) + next((item['perc'] for item in entry['generationmix'] if item['fuel'] == 'solar'), 0)
                }
                all_data.append(row)

            df = pd.DataFrame(all_data)
            df.to_excel(writer, sheet_name=postcode, index=False)

    print("Excel file with separate sheets for each postcode saved successfully.")

def generate_tiles(postcode, base_output_folder):
    print(f"Fetching data for postcode: {postcode}")
    combined_data = fetch_combined_data(postcode)
    
    colored_folder = os.path.join(base_output_folder, "Colored_Tiles")
    transparent_folder = os.path.join(base_output_folder, "Transparent_Tiles")
    
    # Ensure the folders are cleared before generating new tiles
    if os.path.exists(colored_folder):
        for file in os.listdir(colored_folder):
            os.remove(os.path.join(colored_folder, file))

    if os.path.exists(transparent_folder):
        for file in os.listdir(transparent_folder):
            os.remove(os.path.join(transparent_folder, file))

    os.makedirs(colored_folder, exist_ok=True)
    os.makedirs(transparent_folder, exist_ok=True)

    print(f"Colored Tiles folder: {colored_folder}")
    print(f"Transparent Tiles folder: {transparent_folder}")

    for entry in combined_data:
        wind_perc = entry['generationmix'][8]['perc']
        solar_perc = entry['generationmix'][7]['perc']
        combined_renewable_perc = wind_perc + solar_perc
        
        # Ensuring 24-hour format with correct padding
        timestamp = datetime.strptime(entry['from'], "%Y-%m-%dT%H:%MZ").strftime("%Y-%m-%d_%H-%M")

        create_colored_tile(wind_perc, solar_perc, colored_folder, timestamp)
        create_text_tile(combined_renewable_perc, transparent_folder, timestamp)

if __name__ == "__main__":
    postcode = "M9"
    base_output_folder = "C:\\Users\\noelp\\Desktop\\Energy Video\\M9_Tiles"
    generate_tiles(postcode, base_output_folder)
    
    postcodes = ["M9", "M11", "M40", "M12", "M13", "M22", "M23"]
    generate_excel(postcodes, base_output_folder)

