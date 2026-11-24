import requests

base_url = "https://jsonplaceholder.typicode.com"

def explain_status(code):
    messages={
        200:"Success",
        201:"Created successfully",
        400:"Bad request",
        401:"unauthorized",
        404:"Not found",
        500:"internal Server Error"

    }

    return messages.get(code,"Unknow Status Code")



response=requests.get(f"{base_url}/users",timeout=10)
 
users=response.json()
    
for user in users[:5]:
   print(user["id"],"-",user["name"],"-",user["email"])


new_post = {
    "title":"Python Rest API ",
    "body":"Learning API requests",
    "userId":1
   }
response=requests.post(f"{base_url}/posts",json=new_post,timeout=10)
                
print(f"POST: {response.status_code},id: {response.json()['id']}")


updated_post= {
   "Id":1,
   "title":"Updated Python API",
   "body":"Learning Put request",
   "userId":1

}

put_response=requests.put(f"{base_url}/posts/1",json=updated_post,timeout=10)


patch_response=requests.patch(f"{base_url}/posts/1",json={"title":"patched"},timeout=10)

delete_response=requests.delete(f"{base_url}/posts/1",timeout=10)
print(f"PUT: {put_response.status_code} | PATCH: {patch_response.status_code} | DELETE: {delete_response.status_code}")
not_found=requests.get(f"{base_url}/posts/9999",timeout=10)
print(f"GET /posts/9999 -> {not_found.status_code} {explain_status(not_found.status_code)}")
    



for code in [200,201,400,401,404,500]:
    print(code,"_",explain_status(code))

