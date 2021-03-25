Instruction to access the database:
1. Download the MongoDB Compass application in the link: https://www.mongodb.com/try/download/compass
2. Open the application, select new connection, and paste in the following connection string: mongodb+srv://Ripple:wisconsinmadison@cluster0.qztag.mongodb.net/test
3. Wait for the connection and then you should be able to view the data stored inside

Instruction to install Flask and Pymongo:
1. pip install -U Flask
2. pip install pymongo


/reportCreate
Request
{ 
    "IncidentID": "123455",
    "StreetName": "StateStreet",
    "Location": "xxxx",
    "Year": "2020",
    "Month": "6",
    "Day": "9",
    "Description": "xxxx",
    "Category": "sss"
}
Response
{
    "Msg": "Success",
    "Status": true
}

/deleteReportByID
Request
{
    "IncidentID": "123455"
}
Response
{
    "Msg": "Success",
    "Status": true
}

/getReportByCategory
Request
{
    "Category": "xxxx"
}
Response
[
    {
        "Category": "sss",
        "Day": "9",
        "Description": "xxxx",
        "IncidentID": "123455",
        "Location": "xxxx",
        "Month": "6",
        "Year": "2020",
        "StreetName": "StateStreet"
    }
]


/getReportByDate
Request
{
    "BeginYear": "2020",
    "BeginMonth": "1",
    "BeginDay": "1",
    "EndYear": "2021",
    "EndMonth": "12",
    "EndDay": "3"
}
Response
{
    "Data": [
        {
            "Category": "sss",
            "Day": "9",
            "Description": "xxxx",
            "IncidentID": "IncidentID",
            "Location": "xxxx",
            "Month": "6",
            "Year": "2020",
            "StreetName": "StateStreet"
        }
    ],
    "Msg": "Success",
    "Status": true
}


/getReportByLocation
Resquest
{ 
    "StreetName": "StateStreet"
}
Response
{
    "Data": [
        {
            "Category": "sss",
            "Day": "9",
            "Description": "xxxx",
            "IncidentID": "IncidentID",
            "Location": "xxxx",
            "Month": "6",
            "StreetName": "StateStreet",
            "Year": "2020"
        }
    ],
    "Msg": "Success",
    "Status": true
}
