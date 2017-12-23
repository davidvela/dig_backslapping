import requests
import facebook

import urllib
from urllib.parse import urlparse
import subprocess
import warnings

print("hi Facebook")

def get_fb_token(app_id, app_secret):           
    payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
    #print file.text #to test what the FB api responded with    
    print(file)
    result = file.text.split("=")[1]
    #print file.text #to test the TOKEN
    return result

def get_fb_token2(app_id, app_secret, prof):           

    # Hide deprecation warnings. The facebook module isn't that up-to-date (facebook.GraphAPIError).
    warnings.filterwarnings('ignore', category=DeprecationWarning)


    # Parameters of your app and the id of the profile you want to mess with.
    FACEBOOK_APP_ID     = app_id
    FACEBOOK_APP_SECRET = app_secret
    FACEBOOK_PROFILE_ID = prof


    # Trying to get an access token. Very awkward.
    oauth_args = dict(client_id     = FACEBOOK_APP_ID,
                    client_secret = FACEBOOK_APP_SECRET,
                    grant_type    = 'client_credentials')
    oauth_curl_cmd = ['curl',
                    'https://graph.facebook.com/oauth/access_token?' + urllib.parse.urlencode(oauth_args)]
    oauth_response = subprocess.Popen(oauth_curl_cmd,
                                    stdout = subprocess.PIPE,
                                    stderr = subprocess.PIPE).communicate()[0]
    print(oauth_response)
    try:
        oauth_access_token = urlparse.parse_qs(str(oauth_response))['access_token'][0]
    except KeyError:
        print('Unable to grab an access token!')
        exit()
    return oauth_access_token
    # facebook_graph = facebook.GraphAPI(oauth_access_token)


    # # Try to post something on the wall.
    # try:
    #     fb_response = facebook_graph.put_wall_post('Hello from Python', \
    #                                             profile_id = FACEBOOK_PROFILE_ID)
    #     print fb_response
    # except facebook.GraphAPIError as e:
    #     print 'Something went wrong:', e.type, e.message
        

# appid = "s"
# appsecret = ""
# profid = ""
# token = get_fb_token2(appid, appsecret, profid)
# token : https://developers.facebook.com/tools/explorer

token = "daskla"
graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
print(profile)

print("LIST OF FRIENDS:")
# friends =  graph.get_object("me/friends") 
friends = graph.get_connections("me", "friends")
# friends = graph.get_connections("me", "taggable_friends")
friend_list = [friend['name'] for friend in friends['data']]


print(friends["summary"])
print(friends)
while(True):
    for friend in friends["data"]: 
        friend_list = [friend['name'] for friend in friends['data']]
        print(friend_list)
    if 'paging' in friends and 'next' in friends['paging']:
        print("get next")
        friends = requests.get(friends['paging']['next']).json
    else: 
        break

print("\n OTHER:")
feed =  graph.get_object("me/books") #photos, books, feed
print(feed)

print("\n OTHER2:")
posts = graph.get_connections(profile['id'], 'posts')
print(posts)

# post a comment in my wall 
#graph.put_object(parent_object='me', connection_name='feed', message='Hello, world from Python Facebook-sdk ')
# graph.put_object(parent_object='rhema.rajendram', connection_name='feed', message='Hello, world from Python Facebook-sdk ')


# I can't get my list of friends unless they accept with the user_friend policies 
# read_friendlists Renamed - We renamd the read_friendlists permission to read_custom_friendlists. 
# See Facebook Platform Changelog, API version 2.3. You'll need to specify read_custom_friendlists in the Login Dialog 
# from v2.3 onwards. For people who granted read_friendlists in previous versions, this will be returned as read_custom_friendlists
# when calling /me/permissions in v2.3 and up.

