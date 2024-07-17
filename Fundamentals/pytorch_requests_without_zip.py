## import raw from github
import requests
from pathlib import Path #create file directory

# setup path to data folder
data_path = Path("data/")
file_path = data_path / "vol7"

# if the folder doesn't exist, download and prepare
if file_path.is_dir():
  print(f"{file_path} directory already exists... skipping download")
else:
  print(f"{file_path} does not exist, creating one...")
  file_path.mkdir(parents=True, exist_ok=True)


# Download the data
with open(data_path / "vol7.json", "wb") as f:
  ## raw github or API link
  request = requests.get("https://raw.githubusercontent.com/wjbmattingly/bap_sent_embedding/main/data/vol7.json")
  print("Downloading dataset....")
  f.write(request.content) # write content of request to file 
