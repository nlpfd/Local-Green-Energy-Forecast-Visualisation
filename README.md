# Local Green Energy Forecast Visualization

This project leverages the National Grid ESO Carbon Intensity API to forecast energy fuel mix and carbon intensity measurements at the postcode level, half-hourly, for the next 48 hours. The project specifically focuses on low-income areas in the UK, which may be at risk of being left behind during the energy transition. The forecast includes a calculation of the combined wind and solar energy percentage.

## Features

- **48-Hour Energy Forecast**: Retrieves data from the Carbon Intensity API for specific postcodes and generates an Excel file with half-hourly energy fuel mix forecasts.
- **Tile Visualisation**:
  - **Colored Tiles**: Visual representations of the combined wind and solar energy percentages, with shades of green and grey indicating renewable energy contributions.
  - **Transparent Text Tiles**: Overlay-ready tiles displaying the location, wind and solar combined percentage, date, and time, suitable for charts, video loops, GIFs, or other visualisation applications.
- **Social Impact**: Highlights energy disparities in low-income areas, providing a tool for raising awareness and advocating for equitable access to renewable energy.

## Installation

To use this project, you’ll need to have Python installed on your machine along with the required Python packages.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nlptfld/nlptfld-Local-Green-Energy-Forecast-Visualisation.git
   cd nlptfld-Local-Green-Energy-Forecast-Visualisation
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the following packages installed:
   - `requests`
   - `Pillow`
   - `pandas`
   - `xlsxwriter`

3. **Run the Code**:
   Update the `postcode` and `postcodes` variables in the script to your desired locations and run the code to generate the energy forecast and visualisation tiles.
   ```bash
   python main.py
   ```

## Usage

### 1. Generate Energy Forecast

The script fetches energy data for specified postcodes and saves it in an Excel file with separate sheets for each postcode. The data includes the percentage contribution of various fuel sources, including nuclear, gas, biomass, wind, solar, and more.

### 2. Create Visualisation Tiles

The script generates two types of tiles:

- **Colored Tiles**: Representing the combined wind and solar energy percentages.
- **Transparent Text Tiles**: Featuring text overlays with location, wind and solar percentage, date, and time.

These tiles can be used to create dynamic visualisations, such as video loops or GIFs, to illustrate the energy forecast for specific areas.

### 3. Customize and Extend

The code can be customized to include additional data points or to generate different types of visualizations. Contributions are welcome!

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
