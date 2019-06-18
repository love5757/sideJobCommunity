## How to run this
 
1) Start the server by running `npm start`

2) Check the swagger-ui on `http://localhost:3000/docs`

3) GET `http://localhost:3000/getRecruitList` 

4) GET `http://localhost:3000/getRecruitDetail?id=${recr_id}` 

5) POST `http://localhost:3000/insertRecruiting` with the following body
````
{
  "recr_id" : {id}
}
````

6) POST `http://localhost:3000/updateHit` with the following body
````
{
  "recr_id" : {id}
}
````

````
{
  "name": "test",
  "location": "test",
  "kakao_id": "test",
  "kakao_name": "test",
  "email": "test",
  "phone": "test",
  "type": "test",
  "title": "test",
  "content": "test",
  "stock_opt": "test",
  "skill": "test",
  "url": "test",
  "period": "test",
  "price": "test",
  "years": "test",
  "sector": "test",
  "from_home": "test",
  "more_detail": "test"
}
````