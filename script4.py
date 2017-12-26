import requests
import facebook

# delete posts: 
posts = [ {
      "message": "Merry X-Mas person: 19",
      "created_time": "2017-12-26T00:31:12+0000",
      "id": "10214714467041135_10215338574683436"
    },
    {
      "message": "Merry X-Mas person: 18",
      "created_time": "2017-12-26T00:31:10+0000",
      "id": "10214714467041135_10215338574443430"
    },
    {
      "message": "Merry X-Mas person: 17",
      "created_time": "2017-12-26T00:31:08+0000",
      "id": "10214714467041135_10215338573803414"
    },
    {
      "message": "Merry X-Mas person: 16",
      "created_time": "2017-12-26T00:31:07+0000",
      "id": "10214714467041135_10215338573483406"
    },
    {
      "message": "Merry X-Mas person: 15",
      "created_time": "2017-12-26T00:31:05+0000",
      "id": "10214714467041135_10215338573203399"
    },
    {
      "message": "Merry X-Mas person: 14",
      "created_time": "2017-12-26T00:31:04+0000",
      "id": "10214714467041135_10215338573043395"
    },
    {
      "message": "Merry X-Mas person: 13",
      "created_time": "2017-12-26T00:31:02+0000",
      "id": "10214714467041135_10215338572803389"
    },
    {
      "message": "Merry X-Mas person: 12",
      "created_time": "2017-12-26T00:31:01+0000",
      "id": "10214714467041135_10215338572443380"
    },
    {
      "message": "Merry X-Mas person: 11",
      "created_time": "2017-12-26T00:30:59+0000",
      "id": "10214714467041135_10215338572203374"
    },
    {
      "message": "Merry X-Mas person: 10",
      "created_time": "2017-12-26T00:30:57+0000",
      "id": "10214714467041135_10215338571963368"
    },
    {
      "message": "Merry X-Mas person: 9",
      "created_time": "2017-12-26T00:30:55+0000",
      "id": "10214714467041135_10215338571643360"
    },
    {
      "message": "Merry X-Mas person: 8",
      "created_time": "2017-12-26T00:30:53+0000",
      "id": "10214714467041135_10215338571443355"
    },
    {
      "message": "Merry X-Mas person: 7",
      "created_time": "2017-12-26T00:30:51+0000",
      "id": "10214714467041135_10215338571163348"
    },
    {
      "message": "Merry X-Mas person: 6",
      "created_time": "2017-12-26T00:30:50+0000",
      "id": "10214714467041135_10215338571003344"
    },
    {
      "message": "Merry X-Mas person: 5",
      "created_time": "2017-12-26T00:30:48+0000",
      "id": "10214714467041135_10215338570723337"
    },
    {
      "message": "Merry X-Mas person: 4",
      "created_time": "2017-12-26T00:30:46+0000",
      "id": "10214714467041135_10215338570523332"
    }
    # { test 
    #   "message": "Merry X-Mas person: 3", 
    #   "created_time": "2017-12-26T00:30:44+0000",
    #   "id": "10214714467041135_10215338570323327"  #10214714467041135_10215338812649385 
    # }
  ]


token = "ajdaljdaslk"
graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
print(profile)

post_id = ""
for i in posts: 
    print(i["id"])
    post_id = i["id"]
    graph.delete_object(id=post_id)
