
from datetime import datetime
import httpx
import pygeohash as pgh
from geopy import Photon
import random
import uuid

android_id = random.randint(10 ** (16 - 1), (10 ** 16) - 1)
# NOTE: 16 zeros ID is banned

channel = "GLOBAL"
abi_type = 2
total_mem_bytes = 5000000000
sc_height = 1080
sc_width = 720
advertising_id = str(uuid.uuid4())
major_version = 9
minor_version = 17
patch_version = 2
build_number = 118509
version = "%s.%s.%s.%s" % (major_version, minor_version, patch_version, build_number)
android_number = 13
client_type = "Unlimited"
phone_model = "Plus"
manufacturer = "Google"

def load_credentials(file='credentials.txt'):
    try:
        with open(file, 'r') as file:
            lines = file.readlines()
            email = lines[0].strip()
            password = lines[1].strip()
            return email, password
    except FileNotFoundError:
        print(f"File {file} not found.")
    except IndexError:
        print("Unexpected file format.")
    return None, None

def grindr_geohash(lat, lon):
    return pgh.encode(lat, lon, precision=12)

def invert(dictionary):
    return {v: k for k, v in dictionary.items()}

woke_terminology_map = {0: 'invalid', 1: 'Man', 2: 'Woman', 3: 'Non-binary', 4: 'Cis Man', 5: 'Trans Man',
                        6: 'Cis Woman', 7: 'Trans Woman', 8: 'Non-Conforming', 9: 'Genderqueer', 10: 'Agender',
                        11: 'Androgynous', 12: 'Bigender', 13: 'Genderfluid', 14: 'Questioning', 15: 'Crossdresser',
                        16: 'Queer', 17: 'Pangender', 18: 'Transfeminine', 19: 'Transmasculine', 20: 'Enby',
                        21: 'Two-Spirit', 22: 'Hijra', 23: 'Kinner', 24: 'Jogappa', 25: 'Kothi', 26: 'Mangalmukhi',
                        27: 'Yì fu zhe', 28: 'Weiniang', 29: 'Demiwoman', 30: 'Demiman', 31: 'Transgenderqueer',
                        32: 'Travesti', 33: 'Kathoey', 34: 'Saaw Praphet Soong', 35: 'Tom', 36: 'Phet Thi Sam',
                        37: 'Bakla', 38: 'Bading/Beki', 39: 'Binabae', 40: 'Bayot', 41: 'Agi', 42: 'Bantut',
                        43: 'Aravani', 44: 'Jogtha', 45: 'Nupa manba', 46: 'Nupi manbi', 47: 'Thirunangai',
                        48: 'Thirunambi', 49: 'Yao', 50: 'Waria', 51: 'Feminiello', 52: 'Transnita', 53: 'Berbeza',
                        54: 'Translaki', 55: 'Third Gender', 56: 'X Gender', 57: 'Buê đuê', 58: 'Enchaquirado',
                        59: 'Muxe', 60: 'Tida Wena', 61: 'Omeguit'}

s = invert(woke_terminology_map)
sexual_pos_dict = {
    1: "Top",
    2: "Bottom",
    3: "Versatile",
    4: "Versatile Bottom",
    5: "Versatile Top",
    6: "Side"
}

rel_status_dict = {
    1: "Single",
    2: "Dating",
    3: "Exclusive",
    4: "Committed",
    5: "Partnered",
    6: "Engaged",
    7: "Married",
    8: "Open Relationship",
}

body_type_dict = {
    1: "Toned",
    2: "Average",
    3: "Large",
    4: "Muscular",
    5: "Slim",
    6: "Stocky"
}

looking_for_dict = {
    2: "Chat",
    3: "Dates",
    4: "Friends",
    5: "Networking",
    6: "Relationship",
    7: "Hookups",
}

looking_for_dict_inv = invert(looking_for_dict)

ethnicity_dict = {
    1: "Asian",
    2: "Black",
    3: "Latino",
    4: "Middle Eastern",
    5: "Mixed",
    6: "Native American",
    7: "White",
    8: "Other",
    9: "South Asian"
}

tribes_dict = {
    1: "Bear",
    2: "Clean Cut",
    3: "Daddy",
    4: "Discreet",
    5: "Geek",
    6: "Jock",
    7: "Leather",
    8: "Otter",
    9: "Poz",
    10: "Rugged",
    11: "Trans",
    12: "Twink",
    13: "Sober"
}

tribes_dict_inv = invert(tribes_dict)

report_reason_dict = {
    1: "Offensive Profile Image",
    2: "Offensive Profile Text",
    4: "Abusive User",
    5: "Solicitation Spam",
    7: "Under Age",
    10: "Impersonation"
}

hiv_dict = {
    1: "Negative",
    2: "Negative on PrEP",
    3: "Positive",
    4: "Positive Undetectable"
}

nsfw_dict = {
    1: "Never",
    2: "Not at First",
    3: "Yes"
}

meet_at_dict = {
    1: "My Place",
    2: "Your Place",
    3: "Bar",
    4: "Coffee Shop",
    5: "Restaurant"
}

pronouns_dict = {
    0: "No Response",
    1: "Custom Pronouns",
    2: "He/Him/His",
    3: "She/Her/Hers",
    4: "They/Them/Theirs"
}

# Gender
gender_dict = {
    0: "No Response",
    1: "Man",
    2: "Cis Man",
    3: "Trans Man",
    4: "Custom Man",
    5: "Woman",
    6: "Cis Woman",
    7: "Trans Woman",
    8: "Custom Woman",
    9: "Non Binary",
    10: "Non Conforming",
    11: "Queer",
    12: "Crossdresser",
    13: "Custom Non-Binary"
}

vaccine_dict = {
    1: "COVID-19",
    2: "Monkeypox",
    3: "Meningitis"
}

sexual_pos_dict_inv = invert(sexual_pos_dict)
looking_for_dict_inv = invert(looking_for_dict)
tribes_dict_inv = invert(tribes_dict)
rel_status_dict_inv = invert(rel_status_dict)
body_type_dict_inv = invert(body_type_dict)
ethnicity_dict_inv = invert(ethnicity_dict)
report_reason_dict_inv = invert(report_reason_dict)
hiv_dict_inv = invert(hiv_dict)
nsfw_dict_inv = invert(nsfw_dict)
meet_at_dict_inv = invert(meet_at_dict)
pronouns_dict_inv = invert(pronouns_dict)
gender_dict_inv = invert(gender_dict)
vaccine_dict_inv = invert(vaccine_dict)

tags = ['adventurous', 'anime', 'anon', 'art', 'bb', 'beach', 'bear', 'beard', 'bi', 'bondage', 'brunch', 'bubblebutt',
        'carplay', 'catperson', 'chastity', 'chill', 'chub', 'cleancut', 'college', 'commando', 'concerts', 'condoms',
        'condomsonly', 'confident', 'cooking', 'couple', 'cruising', 'cub', 'cuddling', 'curious', 'cut', 'daddy',
        'dancing', 'dating', 'direct', 'dirty', 'discreet', 'diy', 'dl', 'dogperson', 'dom', 'drag', 'drugfree', 'dtf',
        'edging', 'fashion', 'feet', 'femme', 'ff', 'flexible', 'friends', 'ftm', 'fun', 'furries', 'fwb', 'gaming',
        'gaymer', 'gear', 'geek', 'gh', 'goofy', 'group', 'hairy', 'hands', 'hiking', 'hosting', 'hung', 'jo', 'jock',
        'karaoke', 'kind', 'kink', 'kissing', 'latex', 'leather', 'lesbian', 'limits', 'lingerie', 'looking', 'loyal',
        'ltr', 'masc', 'mature', 'military', 'monogamy', 'movies', 'mtf', 'muscle', 'music', 'naps', 'nipples',
        'nosmoking', 'nsa', 'nylon', 'oral', 'otter', 'outgoing', 'parent', 'pic4pic', 'piercings', 'pits', 'poly',
        'popmusic', 'poz', 'public', 'pup', 'pupplay', 'quickie', 'reading', 'reliable', 'roleplay', 'romantic',
        'rough', 'rpdr', 'rubber', 'rugged', 'safersex', 'showoff', 'shy', 'sissy', 'smooth', 'sober', 'socks',
        'spanking', 'spit', 'sub', 't4t', 'tattoos', 'tennis', 'tentacles', 'theater', 'thick', 'toys', 'trans', 'tv',
        'twink', 'twunk', 'uc', 'underwear', 'unicorn', 'vanilla', 'videochat', 'visiting', 'watching', 'weightlifting',
        'workingout', 'writing', 'ws', 'yoga']

def comma_join(tribes):
    return ','.join(map(str, tribes))

def location_to_lat_lon(location_name):
    geolocator = Photon(user_agent="myGeocoder")
    location = geolocator.geocode(location_name)
    if location is not None:
        lat, lon = location.latitude, location.longitude
        return lat, lon
    else:
        return None


# Imprime el diccionario cargado desde el archivo JSON
def parse_profile(profile):
    if profile is None or profile['type'] == 'advert_v1':
        return profile
    # full_profile_v1, partial_profile_v1
    profile['lastOnline'] = datetime.fromtimestamp(profile['lastOnline'] / 1000)
    profile['lookingFor'] = [looking_for_dict.get(x, x) for x in profile['lookingFor']]

    if 'tribes' in profile:
        profile['tribes'] = [tribes_dict.get(x, x) for x in profile['tribes']]
    if 'meetAt' in profile:
        profile['meetAt'] = [meet_at_dict.get(x, x) for x in profile['meetAt']]
    if 'vaccines' in profile:
        profile['vaccines'] = [vaccine_dict.get(x, x) for x in profile['vaccines']]

    if 'genders' in profile:
        profile['genders'] = [gender_dict.get(x, x) for x in profile['genders']]
    if 'pronouns' in profile:
        profile['pronouns'] = [pronouns_dict.get(x, x) for x in profile['pronouns']]
    if 'relationshipStatus' in profile:
        profile['relationshipStatus'] = rel_status_dict[profile['relationshipStatus']]
    if 'ethnicity' in profile:
        profile['ethnicity'] = ethnicity_dict[profile['ethnicity']]
    if 'bodyType' in profile:
        profile['bodyType'] = body_type_dict[profile['bodyType']]
    if 'sexualPosition' in profile:
        profile['sexualPosition'] = sexual_pos_dict[profile['sexualPosition']]
    if 'hivStatus' in profile:
        profile['hivStatus'] = hiv_dict[profile['hivStatus']]
    if 'acceptsNsfwPics' in profile:
        profile['acceptsNsfwPics'] = nsfw_dict[profile['acceptsNsfwPics']]
    return profile


# Replace with your desired location name
def login(email, password):
    global auth_token
    with httpx.Client() as client:
        response = client.post(url="https://grindr.mobi/v3/sessions", headers={
            # Minimal Headers
            "L-Device-Info": ("%s;%s;%s;%s;%sx%s;%s" % (
                android_id, channel, abi_type, total_mem_bytes, sc_height, sc_width, advertising_id)),
            "User-Agent": ("grindr3/%s;%s;%s;Android %s;%s;%s" % (
                version, build_number, client_type, android_number, phone_model, manufacturer))
        }, json={"email": email, "password": password, "token": ""})

        response = response.json()
        if 'message' in response:
            # Message types: ACCOUNT_BANNED
            print(response['message'])
        return response

def getCascadePage(lat, lon, online_only=False, photo_only=False, face_only=False, not_recently_chatted=False,
                   has_album=False, age_min=0, age_max=0, height_min=0, height_max=0, weight_min=0, weight_max=0,
                   tribes=[],
                   looking_for=[], rel_statuses=[], body_types=[], sex_pos=[], meet_at=[], nsfw_pics=[], tags=[],
                   fresh=[], page_number=1, genders=[], right_now=False):
    params = {
        "nearbyGeoHash": grindr_geohash(lat, lon),  # Geohash precision 12
        "onlineOnly": online_only,
        "photoOnly": photo_only,
        "faceOnly": face_only,
        "notRecentlyChatted": not_recently_chatted,
        "hasAlbum": has_album,
        "fresh": fresh,
        "pageNumber": page_number,
        "rightNow": right_now,
    }

    if age_min != 0:
        params["ageMin"] = age_min
    if age_max != 0:
        params["ageMax"] = age_max
    if height_min != 0:
        params["heightCmMin"] = height_min
    if height_max != 0:
        params["heightCmMax"] = height_max
    if weight_min != 0:
        params["weightGramsMin"] = weight_min
    if weight_max != 0:
        params["weightGramsMax"] = weight_max
    if tribes is not None and tribes:
        params["tribes"] = comma_join(tribes)
    if looking_for is not None and looking_for:
        params["lookingFor"] = comma_join(looking_for)
    if rel_statuses is not None and rel_statuses:
        params["relationshipStatuses"] = comma_join(rel_statuses)
    if body_types is not None and body_types:
        params["bodyTypes"] = comma_join(body_types)
    if sex_pos is not None and sex_pos:
        params["sexualPositions"] = comma_join(sex_pos)
    if meet_at is not None and meet_at:
        params["meetAt"] = comma_join(meet_at)
    if nsfw_pics is not None and nsfw_pics:
        params["nsfwPics"] = comma_join(nsfw_pics)
    if tags is not None and tags:
        params["tags"] = comma_join(tags)
    if genders is not None and genders:
        params["genders"] = comma_join(genders)

    with httpx.Client() as client:
        response = client.get(url="https://grindr.mobi/v1/cascade", headers=headers, params=params)
        result = response.json()

    return result

# ALBUMS TODO: Implement missing endpoints
def albums_1(album_id, content_id):
    with httpx.Client() as client:
        response = client.get(url=("https://grindr.mobi/v1/albums/%s/content/%s/poster" % (album_id, content_id)), headers=headers)
        result = response.json()

    return result

def red_dot():
    with httpx.Client() as client:
        client.put(url=("https://grindr.mobi/v1/albums/red-dot"), headers=headers)

def getMyAlbums(): # Get my albums
    with httpx.Client() as client:
        response = client.get(url=("https://grindr.mobi/v1/albums/"), headers=headers)
        result = response.json()
    return result

session = login(*load_credentials())
headers = {
    # The commented headers are not required for a good response.
    # "Accept": "application/json",
    # "Accept-Encoding": "gzip",
    # "Accept-language": "Your Language",
    "Authorization": ("Grindr3 %s" % session['sessionId']),
    # "Connection": "Keep-Alive",
    # "Host": "grindr.mobi",
    # "L-Device-Info": ("%s;%s;%s;%s;%sx%s;%s" % (android_id, channel, abi_type, total_mem_bytes, sc_height, sc_width, advertising_id)),
    # "L-Grindr-Roles": "[]",
    # "L-Locale": "Your Locale",
    # "L-Time-Zone": "Your Time Zone",
    "User-Agent": ("grindr3/%s;%s;%s;Android %s;%s;%s" % (
        version, build_number, client_type, android_number, phone_model, manufacturer)),
}

rd = red_dot()

print()