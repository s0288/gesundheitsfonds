Send messages within host network:
- build docker: "docker build -t gesundheitsfonds ."
- start docker: "docker run --rm -it --network host gesundheitsfonds"
- "curl http://127.0.0.1:5000"
- make sure your cronjob is set up

Set up cronjob:
- "crontab -e"

MVP des Gesundheitsfonds:
- Am Anfang schickst du eine Mail mit deinen OKRs und überweist das Geld, das du bereit bist in dich zu investieren. 
- Jeden Sonntag um 19 Uhr erhältst du eine E-Mail mit deinen OKRs. Deine Antworten werden geloggt.
- Am Ende erhältst du eine Mail mit allen Logs und der Bitte um Bewertung deiner OKRs. Wenn du mind. 50% deiner KRs erreicht hast, erhältst du 75% deines Geldes zurück.
