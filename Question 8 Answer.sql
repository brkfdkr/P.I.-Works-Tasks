COALESCE(
    (SELECT MEDIAN(daily_vaccinations) 
     FROM vaccinations AS v2 
     WHERE v2.country = vaccinations.country 
     		AND v2.daily_vaccinations IS NOT NULL),0)