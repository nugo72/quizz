# quizz
მთლიან პროექტში გამოყენებულია ჰაერის დაბინძურების აპი - https://openweathermap.org/api/air-pollution

ბაზაში მონაცემები შეტანილია - Forecast air pollution data - ს მიხედვით.

მონაცემთა ბაზაში შეტანილია ერთგვარი პროგნოზი ჰაერის დაბინძურების მაჩვენებლებისა. 10 დღიანი დიაპაზონი აქვს. სვეტებში ჩავწერე id აუტოინკრემენტით, თარიღი და საათი რომმლის მიხედვით აჩვენებს ამ დაბინძურების მაჩვენებლებს(date დავაიმპორტე და გადავიყვანე თვე,დღე,წელი ზუსტი საათი/წუთი ფორმატში რადგან json-ფაილში unix ფორმატით იყო მონაცემები აი ასე - (მაგ: 1620557407)), და 4 სახის კომპონენტი საკუთარი მაჩვენებლით(co, no, no2, so2)
