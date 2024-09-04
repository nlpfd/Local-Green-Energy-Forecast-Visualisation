# Local Green Energy Forecast Visualisation

This project leverages the National Grid ESO Carbon Intensity API to forecast regional energy fuel mix and carbon intensity measurements using postcode searches, half-hourly, for the next 48 hours. The project specifically focuses on low-income areas in the UK, which may have less access to this information and be at risk of being left behind during the energy transition. The forecast includes a calculation of the combined wind and solar energy percentage.

## Features

- **48-Hour Energy Forecast**: Retrieves data from the Carbon Intensity API using postcode searches and generates an Excel file with half-hourly energy fuel mix forecasts.
- **Tile Generation for Visualisation**:
  - **Colored Tiles**: Visual representations of the combined wind and solar energy percentages, with shades of green and grey indicating renewable energy contributions.
  - **Transparent Text Tiles**: Overlay-ready tiles displaying the location, wind and solar combined percentage, date, and time, suitable for charts, video loops, GIFs, or other visualisation applications.
- **Social Impact**: Postcode searchs for regional forecasts to make this information more accesible by highlighting familiar local areas.
Highlights green energy opportunities for users in low-income areas, providing a tool for raising awareness and advocating for equitable access to renewable energy.

## Installation

To use this project, you’ll need to have Python installed on your machine along with the required Python packages.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nlpfd/Local-Green-Energy-Forecast-Visualisation.git green-energy-forecast
   cd green-energy-forecast
   ```

2. **Install dependencies**:

   You should create a virtual environment (to avoid clashing with the rest of your Python installation) and then activate it.

   - If you are running on Linux, then you could run:

      ```bash
      python -m venv venv
      source venv/bin/activate
      ```

   - If you are running with an Anaconda distribution, you can do this with:
      ```bash
      conda create -n green-energy-forecast
      conda activate green-energy-forecast
      ```

   Then, install the requirements in this environment:

   ```bash
   pip install -r requirements.txt
   ```


3. **Run the Code**:
   Update the `postcode` and `postcodes` variables in the script to your desired locations and run the code to generate the energy forecast and visualisation tiles.
   ```bash
   python main.py
   ```

## Usage

### 1. Generate Energy Forecast

The script fetches forecasted half-hourly energy data for regions via postcode searches for the next 48 hours, and saves it in an Excel file with separate sheets for each postcode. The data includes the percentage contribution of various fuel sources, including nuclear, gas, biomass, wind, solar, and more.

### 2. Create Visualisation Tiles

The script generates two types of tiles:

- **Colored Tiles**: Representing the combined wind and solar energy percentages.
- **Transparent Text Tiles**: Featuring text overlays with location, wind and solar percentage, date, and time.

These tiles can be used to create dynamic visualisations, such as video loops or GIFs, to illustrate the energy forecast for specific areas.

### 3. Customise and Extend

The code can be customised to include additional data points or to generate different types of visualisations. Contributions are welcome!

## Contributing

Contributions are encouraged! If you have ideas for new features, improvements, or want to extend the functionality, feel free to fork the repository and submit a pull request.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **National Grid ESO Carbon Intensity API**: Providing the data that powers this project.
