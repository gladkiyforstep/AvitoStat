# StatProject

 Метод /add принимает поисковую фразу и регион.Возвращает id этой пары, фразу и регион. 
 Пример: POST запрос
 
 {
 
    "phrase":"утюг",    
    "region":"chelyabinskaya_oblast"
    
 }

по адресу http://localhost:8000/api/add/
вернёт


{

    "id":"4",
    "phrase":"утюг", 
    "region":"chelyabinskaya_oblast"    
      
}


Метод /stat Принимает на вход id связки поисковая фраза + регион и интервал(временную метку начала интервала и конца).
Возвращает связку(поисковая фраза + регион)счётчики и соответствующие им временные метки (timestamp).
Пример: GET запрос


{

            "query_id": "4",
            "start_time": "2020-11-19T13:35:09Z",
            "finish_time": "2020-12-14T00:00:00Z"
            
}

по адресу http://localhost:8000/api/stat/
вернёт

{

    "query": "утюг in moskva_i_mo",
    "counters": [
        [
            22943,
            "2020-12-12T12:25:06.656713Z"
        ],
        [
            22937,
            "2020-12-13T11:20:06.750770Z"
        ],
        [
            22928,
            "2020-12-13T11:21:05.830117Z"
        ]
    ]
    
}


