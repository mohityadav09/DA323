import os
import requests


countries = {
    "US": "United States", "IN": "India", "GB": "United Kingdom", "FR": "France", "DE": "Germany",
    "JP": "Japan", "CN": "China", "BR": "Brazil", "ZA": "South Africa", "RU": "Russia",
    "AU": "Australia", "CA": "Canada", "IT": "Italy", "ES": "Spain", "MX": "Mexico",
    "KR": "South Korea", "ID": "Indonesia", "NL": "Netherlands", "SA": "Saudi Arabia", "TR": "Turkey",
    "AR": "Argentina", "CH": "Switzerland", "SE": "Sweden", "NG": "Nigeria", "PL": "Poland",
    "BE": "Belgium", "TH": "Thailand", "IR": "Iran", "AT": "Austria", "PK": "Pakistan",
    "MY": "Malaysia", "PH": "Philippines", "SG": "Singapore", "CO": "Colombia", "BD": "Bangladesh",
    "VN": "Vietnam", "AE": "United Arab Emirates", "GR": "Greece", "UA": "Ukraine", "HK": "Hong Kong",
    "IL": "Israel", "NO": "Norway", "FI": "Finland", "DK": "Denmark", "CL": "Chile",
    "CZ": "Czech Republic", "PT": "Portugal", "RO": "Romania", "HU": "Hungary", "NZ": "New Zealand",
    "IE": "Ireland", "PE": "Peru", "KE": "Kenya", "VE": "Venezuela", "EC": "Ecuador",
    "DZ": "Algeria", "MA": "Morocco", "EG": "Egypt", "GH": "Ghana", "SK": "Slovakia",
    "BG": "Bulgaria", "HR": "Croatia", "LT": "Lithuania", "SI": "Slovenia", "LV": "Latvia",
    "EE": "Estonia", "SR": "Serbia", "BO": "Bolivia", "TT": "Trinidad and Tobago", "KW": "Kuwait",
    "OM": "Oman", "CY": "Cyprus", "LU": "Luxembourg", "MT": "Malta", "PY": "Paraguay",
    "IS": "Iceland", "MU": "Mauritius", "QA": "Qatar", "PA": "Panama", "LK": "Sri Lanka",
    "BH": "Bahrain", "JM": "Jamaica", "DO": "Dominican Republic", "GT": "Guatemala", "UY": "Uruguay",
    "NP": "Nepal", "HN": "Honduras", "SV": "El Salvador", "BZ": "Belize", "MG": "Madagascar"
}

lower_keys = [key.lower() for key in countries.keys()]


def download_mp3(mp3_url, country_name):
    """
    Downloads an MP3 file from the given URL and saves it inside the 'anthems' directory.

    :param mp3_url: str, URL of the MP3 file.
    :param country_name: str, Name of the country (used to name the file).
    """
    # Create 'anthems' directory if it doesn't exist
    os.makedirs("anthems", exist_ok=True)

    # Clean country name for file naming
    safe_name = country_name.lower().replace(" ", "_").replace("-", "_")
    save_path = os.path.join("anthems", f"{safe_name}.mp3")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Referer": "https://nationalanthems.info/",
    }

    try:
        response = requests.get(mp3_url, headers=headers, stream=True)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                for chunk in response.iter_content(1024):  # Download in chunks
                    file.write(chunk)
            print(f"Downloaded: {save_path}")
        else:
            print(f"Failed to download {country_name}'s anthem. HTTP Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {country_name}'s anthem: {e}")

# Example usage
download_mp3("https://nationalanthems.info/de.mp3", "Germany")

for key in lower_keys:
  download_mp3(f"https://nationalanthems.info/{key}.mp3", key)
