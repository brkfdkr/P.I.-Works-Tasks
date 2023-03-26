COALESCE(
    (SELECT MEDIAN(daily_vaccinations) 
     FROM vaccinations AS v_med 
     WHERE v_med.country = vaccinations.country 
     		AND v_med.daily_vaccinations IS NOT NULL),0)