import requests

early = [ "2018{:02d}-hubway-tripdata.zip".format(n) for n in range(1,5) ]
late = [ "2018{:02d}-bluebikes-tripdata.zip".format(n) for n in range(5, 13) ]

zips = early + late

for zip_file in zips:
  r = requests.get("https://s3.amazonaws.com/hubway-data/" + zip_file)

  with open(zip_file, 'wb') as outfile:
    for chunk in r.iter_content(chunk_size=128):
      outfile.write(chunk)
