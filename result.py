from bson import json_util
from bson import BSON
import pymysql
import sys
import json
import pymongo

#db연결
conn = pymongo.MongoClient('localhost', 27018)
db = conn.get_database('animal_Welfare')

connection = pymysql.connect(host='localhost', user='sm6336', password='Qkrals9506!', port=13307 ,db='test', charset='utf8')
curs = connection.cursor(pymysql.cursors.DictCursor)

#argv[1]값을 전화번호로 가져옴
tel = ""
for arg in sys.argv[1]:
        tel += arg

#전화번호의 가장 최근 survey기록을 가져옴
result = db.survey.find_one({"tel":tel},sort=[{'date',  -1}])

#result 값으로 분야별, 전체 점수 산출
if float(result["data"]["poor"])==0:
        poor = 100
elif 0 < float(result["data"]["poor"]) <= 0.5:
        poor = 90
elif 0.5 < float(result["data"]["poor"]) <= 1:
        poor = 80
elif 1 < float(result["data"]["poor"]) <= 2:
        poor = 70
elif 2 < float(result["data"]["poor"]) <= 3:
        poor = 60
elif 3 < float(result["data"]["poor"]) <= 4:
        poor = 50
elif 4 < float(result["data"]["poor"]) <= 5:
        poor = 40
elif 5 < float(result["data"]["poor"]) <= 6:
        poor = 30
elif 6 < float(result["data"]["poor"]) <= 8:
        poor = 20
elif 8 < float(result["data"]["poor"]) <= 10:
        poor = 10
else :
        poor = 0

if result["data"]["water_tank_num"]==1:
	if result["data"]["water_tank_clean"] <= 2:
		if result["data"]["water_tank_time"] == 1:
			water = 100
		else :
			water = 80
	else :
		if result["data"]["water_tank_time"] == 1:
			water = 60
		else :
			water = 45
else:
	if result["data"]["water_tank_clean"] <= 2:
		if result["data"]["water_tank_time"] == 1:
			water = 55
		else :
			water = 40
	else :
		if result["data"]["water_tank_time"] == 1:
			water = 35
		else :
			water = 20

protocol1 = (poor*0.7)+(water*0.3)


if result["data"]["straw_fead_tank"] <= 1 and result["data"]["straw_normal"] <= 1 and result["data"]["straw_resting_place"] <= 1:
	straw = 100
elif result["data"]["straw_fead_tank"] <= 2 and result["data"]["straw_normal"] <= 2 and result["data"]["straw_resting_place"] <= 1:
	straw = 80
elif result["data"]["straw_fead_tank"] <= 3 and result["data"]["straw_normal"] <= 3 and result["data"]["straw_resting_place"] <= 2:
	straw = 60
elif result["data"]["straw_fead_tank"] <= 4 and result["data"]["straw_normal"] <= 4 and result["data"]["straw_resting_place"] <= 3:
	straw = 40
else:
	straw = 20

if float(result["data"]["outward_hygiene"])==0:
	outward_hygiene = 100
elif 0 < float(result["data"]["outward_hygiene"]) <= 3:
	outward_hygiene = 90
elif 3 < float(result["data"]["outward_hygiene"]) <= 6:
	outward_hygiene = 80
elif 6 < float(result["data"]["outward_hygiene"]) <= 9:
	outward_hygiene = 70
elif 9 < float(result["data"]["outward_hygiene"]) <= 13:
	outward_hygiene = 60
elif 13 < float(result["data"]["outward_hygiene"]) <= 18:
	outward_hygiene = 50
elif 18 < float(result["data"]["outward_hygiene"]) <= 23:
	outward_hygiene = 40
elif 23 < float(result["data"]["outward_hygiene"]) <= 29:
	outward_hygiene = 30
elif 29 < float(result["data"]["outward_hygiene"]) <= 37:
	outward_hygiene = 20
elif 37 < float(result["data"]["outward_hygiene"]) <= 52:
	outward_hygiene = 10
else:
	outward_hygiene = 0

rest = (straw*0.5)+(outward_hygiene*0.5)

if result["data"]["shade"]==1:
        if result["data"]["summer_ventilating"] == 1:
                if result["data"]["mist_spray"] == 1:
                        summer_ventilation = 100
                else :
                        summer_ventilation  = 80
        else :
                if result["data"]["mist_spray"] == 1:
                        summer_ventilation  = 60
                else :
                        summer_ventilation  = 45
else:
        if result["data"]["summer_ventilating"] == 1:
                if result["data"]["mist_spray"] == 1:
                        summer_ventilation  = 55
                else :
                        summer_ventilation  = 40
        else :
                if result["data"]["mist_spray"] == 1:
                        summer_ventilation  = 20
                else :
                        summer_ventilation  = 0


if result["data"]["wind_block"]==1:
        if result["data"]["winter_ventilating"] == 1:
                winter_ventilation = 100
        else :
                winter_ventilation = 70
else:
        if result["data"]["winter_ventilating"] == 1:
                winter_ventilation = 40
        else :
                winter_ventilation = 20

if result["data"]["winter_straw"]==1:
        if result["data"]["calf_warm"] == 1:
                if result["data"]["calf_wind_block"] == 1:
                        claf_winter = 100
                else :
                        claf_winter = 80
        else :
                if result["data"]["calf_wind_block"] == 1:
                        claf_winter = 60
                else :
                        claf_winter = 45
else:
        if result["data"]["calf_warm"] == 1:
                if result["data"]["calf_wind_block"] == 1:
                        claf_winter = 55
                else :
                        claf_winter = 40
        else :
                if result["data"]["calf_wind_block"] == 1:
                        claf_winter = 20
                else :
                        claf_winter = 0

if int(result["category"])==1:
	ventilation = (summer_ventilation*0.7)+(winter_ventilation*0.3)
else :
	ventilation = (summer_ventilation*0.35)+(winter_ventilation*0.15)+(claf_winter*0.5)

protocol2 = (rest*0.6)+(ventilation*0.4)


if float(result["data"]["limp"])==0:
	limp = 100
elif 0 < float(result["data"]["limp"]) <= 1.5:
	limp = 90
elif 1.5 < float(result["data"]["limp"]) <= 3:
	limp = 80
elif 3 < float(result["data"]["limp"]) <= 5:
	limp = 70
elif 4 < float(result["data"]["limp"]) <= 7:
	limp = 60
elif 5 < float(result["data"]["limp"]) <= 10:
	limp = 50
elif 10 < float(result["data"]["limp"]) <= 13:
	limp = 40
elif 13 < float(result["data"]["limp"]) <= 20:
	limp = 30
elif 20 < float(result["data"]["limp"]) <= 31:
	limp = 20
elif 31 < float(result["data"]["limp"]) <= 49:
	limp = 10
else:
	limp = 0

if float(result["data"]["hair_loss"]) == 0:
	hair_loss = 100
elif 0 < float(result["data"]["hair_loss"]) <= 4:
	hair_loss = 90
elif 0 < float(result["data"]["hair_loss"]) <= 8:
	hair_loss = 80
elif 0 < float(result["data"]["hair_loss"]) <= 13:
	hair_loss = 70
elif 0 < float(result["data"]["hair_loss"]) <= 18:
	hair_loss = 60
elif 0 < float(result["data"]["hair_loss"]) <= 24:
	hair_loss = 50
elif 0 < float(result["data"]["hair_loss"]) <= 31:
	hair_loss = 40
elif 0 < float(result["data"]["hair_loss"]) <= 40:
	hair_loss = 30
elif 0 < float(result["data"]["hair_loss"]) <= 52:
	hair_loss = 20
elif 0 < float(result["data"]["hair_loss"]) <= 72:
	hair_loss = 10
else :
	hair_loss = 0

minimization_of_injury = (limp*0.6)+(hair_loss*0.4)

care = 0
warning = 0

if 5 < float(result["data"]["runny_nose"]) <= 10 or 3 < float(result["data"]["ophthalmic_secretion"]) <= 6 :
	care = care+1
elif 10 < float(result["data"]["runny_nose"]) or 6 < float(result["data"]["ophthalmic_secretion"]):
	warning = warning+1

if 4 < (float(result["data"]["cough"])/int(result["num_of_sample"]))*100 <= 8 or 5 < float(result["data"]["respiratory_failure"]) <= 10 :
	care = care+1
elif 8 < (float(result["data"]["cough"])/int(result["num_of_sample"]))*100 or 10 < float(result["data"]["respiratory_failure"]):
	warning = warning+1

if 5 < float(result["data"]["ruminant"]) <= 10 or 3 < float(result["data"]["diarrhea"]) <= 6 :
	care = care+1
elif 10 < float(result["data"]["ruminant"]) or 6 < float(result["data"]["diarrhea"]):
	warning = warning+1

if 2 < float(result["data"]["fall_dead"]) <= 4:
	care = care+1
elif 4 < float(result["data"]["fall_dead"]):
	warning = warning+1

disease = (100/4)*(4-((care+(3*warning)))/3)

if result["data"]["horn"] == 1:
	horn_removal = 100
elif result["data"]["horn"] == 2:
	if result["data"]["horn_anesthesia"] == 1:
		if result["data"]["horn_painkiller"] == 1:
			horn_removal = 75
		else :
			horn_removal = 52
	else :
		horn_removal = 28
elif result["data"]["horn"] == 3:
	if result["data"]["horn_anesthesia"] == 1:
		if result["data"]["horn_painkiller"] == 1:
			horn_removal = 58
		else :
			horn_removal = 39
	else :
		horn_removal = 20
else:
	if result["data"]["horn_anesthsia"] == 1:
		if result["data"]["horn_painkiller"] == 1:
			horn_removal = 27
		else :
			horn_removal = 17
	else :
		horn_removal = 2


if result["data"]["castration"] == 1:
        castration = 100
elif result["data"]["castration"] == 2:
        if result["data"]["castration_anesthesia"] == 1:
                if result["data"]["castration_painkiller"] == 1:
                        castration = 21
                else :
                        castration = 17
        else :
                castration = 2
elif result["data"]["castration"] == 3:
        if result["data"]["castration_anesthesia"] == 1:
                if result["data"]["castration_painkiller"] == 1:
                        castration = 35
                else :
                        castration = 21
        else :
                castration = 0
else :
        if result["data"]["castration_anesthsia"] == 1:
                if result["data"]["castration_painkiller"] == 1:
                        castration = 34
                else :
                        castration = 21
        else :
                castration = 0


pain = (horn_removal*0.7)+(castration*0.3)

protocol3 = (minimization_of_injury*3.5) + (disease*4) + (pain * 2.5)



struggle_ratio = (result["data"]["struggle"]/(result["data"]["struggle"]+result["data"]["harmony"]))*100

if result["data"]["struggle"] <= 0.5:
        if struggle_ratio == 100 :
                struggle = 58
        elif 100 > struggle_ratio >= 90:
                struggle = 62
        elif 90 > struggle_ratio >= 80:
                struggle = 67
        elif 80 > struggle_ratio >= 70:
                struggle = 73
        elif 70 > struggle_ratio >= 60:
                struggle = 78
        elif 60 > struggle_ratio >= 50:
                struggle = 83
        elif 50 > struggle_ratio >= 40:
                struggle = 87
        elif 40 > struggle_ratio >= 30:
                struggle = 91
        elif 30 > struggle_ratio >= 20:
                struggle = 93
        elif 20 > struggle_ratio >= 10:
                struggle = 95
        else:
                struggle = 100
elif 0.5 < result["data"]["struggle"] <= 1.5:
        if struggle_ratio == 100 :
                struggle = 34
        elif 100 > struggle_ratio >= 90:
                struggle = 41
        elif 90 > struggle_ratio >= 80:
                struggle = 47
        elif 80 > struggle_ratio >= 70:
                struggle = 52
        elif 70 > struggle_ratio >= 60:
                struggle = 57
        elif 60 > struggle_ratio >= 50:
                struggle = 61
        elif 50 > struggle_ratio >= 40:
                struggle = 65
        elif 40 > struggle_ratio >= 30:
                struggle = 67
        elif 30 > struggle_ratio >= 20:
                struggle = 69
        elif 20 > struggle_ratio >= 10:
                struggle = 72
        else:
                struggle = 100
elif 1.5 < result["data"]["struggle"] <= 3:
        if struggle_ratio == 100 :
                struggle = 25
        elif 100 > struggle_ratio >= 90:
                struggle = 30
        elif 90 > struggle_ratio >= 80:
                struggle = 35
        elif 80 > struggle_ratio >= 70:
                struggle = 39
        elif 70 > struggle_ratio >= 60:
                struggle = 42
        elif 60 > struggle_ratio >= 50:
                struggle = 45
        elif 50 > struggle_ratio >= 40:
                struggle = 47
        elif 40 > struggle_ratio >= 30:
                struggle = 48
        elif 30 > struggle_ratio >= 20:
                struggle = 49
        elif 20 > struggle_ratio >= 10:
                struggle = 52
        else:
                struggle = 100
elif 3 < result["data"]["struggle"] <= 8:
        if struggle_ratio == 100 :
                struggle = 8
        elif 100 > struggle_ratio >= 90:
                struggle = 13
        elif 90 > struggle_ratio >= 80:
                struggle = 16
        elif 80 > struggle_ratio >= 70:
                struggle = 19
        elif 70 > struggle_ratio >= 60:
                struggle = 22
        elif 60 > struggle_ratio >= 50:
                struggle = 24
        elif 50 > struggle_ratio >= 40:
                struggle = 20
        elif 40 > struggle_ratio >= 30:
                struggle = 27
        elif 30 > struggle_ratio >= 20:
                struggle = 28
        elif 20 > struggle_ratio >= 10:
                struggle = 30
        else:
                struggle = 100
else :
        if struggle_ratio == 100 :
                struggle = 0
        elif 100 > struggle_ratio >= 90:
                struggle = 3
        elif 90 > struggle_ratio >= 80:
                struggle = 3
        elif 80 > struggle_ratio >= 70:
                struggle = 4
        elif 70 > struggle_ratio >= 60:
                struggle = 5
        elif 60 > struggle_ratio >= 50:
                struggle = 6
        elif 50 > struggle_ratio >= 40:
                struggle = 6
        elif 40 > struggle_ratio >= 30:
                struggle = 6
        elif 30 > struggle_ratio >= 20:
                struggle = 7
        elif 20 > struggle_ratio >= 10:
                struggle = 8
        else:
                struggle = 100

untouchable_cow = (result["data"]["touch_near"]+(3*result["data"]["touch_far"])+(5*result["data"]["touch_impossibility"]))/5

if untouchable_cow == 0:
        comfortable = 0
elif 0 < untouchable_cow <= 7:
        comfortable = 5
elif 7 < untouchable_cow <= 13:
        comfortable = 10
elif 13 < untouchable_cow <= 18:
        comfortable = 15
elif 18 < untouchable_cow <= 22:
        comfortable = 20
elif 22 < untouchable_cow <= 26:
        comfortable = 25
elif 26 < untouchable_cow <= 29:
        comfortable = 30
elif 29 < untouchable_cow <= 32:
        comfortable = 35
elif 32 < untouchable_cow <= 35:
        comfortable = 40
elif 35 < untouchable_cow <= 38:
        comfortable = 45
elif 38 < untouchable_cow <= 41:
        comfortable = 50
elif 41 < untouchable_cow <= 45:
        comfortable = 55
elif 45 < untouchable_cow <= 49:
        comfortable = 60
elif 49 < untouchable_cow <= 54:
        comfortable = 65
elif 54 < untouchable_cow <= 59:
        comfortable = 70
elif 59 < untouchable_cow <= 66:
        comfortable = 75
elif 66 < untouchable_cow <= 73:
        comfortable = 80
elif 73 < untouchable_cow <= 80:
        comfortable = 85
elif 80 < untouchable_cow <= 86:
        comfortable = 90
elif 86 < untouchable_cow <= 93:
        comfortable = 95
else :
        comfortable = 100


protocol4 = (struggle*6.5)+(comfortable*3.5)

total = protocol1+protocol2+protocol3+protocol4

protocol1_info=[]
protocol2_info=[]
protocol3_info=[]
protocol4_info=[]

"""
#survey기록으로 세부 주의사항을 알려줌
for info in db.result_info.find():
        if eval(info['scope_list']):
                if info['category'] == "protocol1" :
                         protocol1_info.append(info['info'])
                elif info['category'] == "protocol2" :
                         protocol2_info.append(info['info'])
                elif info['category'] == "protocol3" :
                         protocol3_info.append(info['info'])
                elif info['category'] == "protocol4" :
                         protocol4_info.append(info['info'])
"""
sql = "select * from result_info"
curs.execute(sql)

rows = curs.fetchall()
for row in rows:
        if eval(row['scope_list']):
                if row['category'] == "protocol1" :
                         protocol1_info.append(row['info'])
                elif row['category'] == "protocol2" :
                         protocol2_info.append(row['info'])
                elif row['category'] == "protocol3" :
                         protocol3_info.append(row['info'])
                elif row['category'] == "protocol4" :
                         protocol4_info.append(row['info'])


#출력
#print (result, protocol1, protocol2, protocol3, protocol4, total)
print (json.dumps({"result":result, "protocol1":int(protocol1), "protocol2":int(protocol2), "protocol3":int(protocol3), "protocol4":int(protocol4), "total":int(total), "protocol1_info":protocol1_info,"protocol2_info":protocol2_info,"protocol3_info":protocol3_info,"protocol4_info":protocol4_info,"protocol1_length":len(protocol1_info),"protocol2_length":len(protocol2_info),"protocol3_length":len(protocol3_info),"protocol4_length":len(protocol4_info)},default=json_util.default,ensure_ascii=False))

