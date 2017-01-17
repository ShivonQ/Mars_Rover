from nasa_mars_rover_client import *
from database import DbHandler
import parse_reqs
NMC = NasaMarsClient()
# db = DbHandler(NMC)
# req='rover_name=Curiosity&search_date=2017-01-01'
# pr=parse_reqs.parse_name_and_date(req)
# print(pr)
three_cams_data=[]
for num in range(3):
    record = NMC.date_image_query('2016-10-27',num,'Curiosity')
    three_cams_data.append(record)
    print(three_cams_data)
# # record = {'img_src': ['http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01310/opgs/edr/rcam/RLB_513788151EDR_F0540238RHAZ00313M_.JPG', 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01310/opgs/edr/rcam/RRB_513788151EDR_F0540238RHAZ00313M_.JPG', 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01310/opgs/edr/rcam/RLB_513781857EDR_F0540088RHAZ00323M_.JPG', 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01310/opgs/edr/rcam/RRB_513781857EDR_F0540088RHAZ00323M_.JPG'], 'earth_date': '2016-04-13', 'rover': 'Curiosity'}
# db.save_photo_data(record)
# manifest = NMC.mission_manifest_data(2)
#
# db.save_mission_manifest_data(manifest)
# db.update_mission_manifest()
# NMC.mission_manifest_data(2)
# db.update_mission_manifest()