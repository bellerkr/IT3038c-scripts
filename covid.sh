POSITIVE=$(curl https://api.covidtracking.com/v1/us/current.json |jq '.[0].positive')
NEGATIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].negative')
DEATHS=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].deaths')
HOSPITALIZED=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].hospitalized')
POSITIVEINCREASE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].positiveincrease')
DEATHINCREASE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].DEATHINCREASE')
PENDING=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].PENDING')

TODAY=$(date)

echo "on $TODAY, there were $POSITIVE positive COVID cases, there were $NEGATIVE negative cases, $DEATHS deaths, $HOSPITALIZED hospitalized, a positive increase of $POSITIVEINCREASE, a death increase of $DEATHINCREASE, and $PENDING pending tests."

