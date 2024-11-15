Variables stored in separate files (Header+values)

Filename

	Data_separate_files_header_startdate(YYYYMMDD)_enddate(YYYYMMDD)_userid_randomstring_currrentdate(YYYYMMDD).zip
	
	e.g., Data_separate_files_header_20050316_20050601.zip

	
Folder structure

	Networkname
		Stationname

		
Dataset Filename

	CSE_Network_Station_Variablename_depthfrom_depthto_startdate_enddate.ext

	CSE	- Continental Scale Experiment (CSE) acronym, if not applicable use Networkname
	Network	- Network abbreviation (e.g., OZNET)
	Station	- Station name (e.g., Widgiewa)
	Variablename - Name of the variable in the file (e.g., Soil-Moisture)
	depthfrom - Depth in the ground in which the variable was observed (upper boundary)
	depthto	- Depth in the ground in which the variable was observed (lower boundary)
	startdate -	Date of the first dataset in the file (format YYYYMMDD)
	enddate	- Date of the last dataset in the file (format YYYYMMDD)
	ext	- Extension .stm (Soil Temperature and Soil Moisture Data Set see CEOP standard)
	
	e.g., OZNET_OZNET_Widgiewa_Soil-Temperature_0.150000_0.150000_20010103_20090812.stm

	
File Content Sample
	
	REMEDHUS   REMEDHUS        Zamarron          41.24100    -5.54300  855.00    0.05    0.05  (Header)
	2005/03/16 00:00    10.30 U	M	(Records)
	2005/03/16 01:00     9.80 U M

	
Header

	CSE Identifier - Continental Scale Experiment (CSE) acronym, if not applicable use Networkname
	Network	- Network abbreviation (e.g., OZNET)
	Station	- Station name (e.g., Widgiewa)
	Latitude - Decimal degrees. South is negative.
	Longitude - Decimal degrees. West is negative.
	Elevation - Meters above sea level
	Depth from - Depth in the ground in which the variable was observed (upper boundary)
	Depth to - Depth in the ground in which the variable was observed (lower boundary)

	
Record

	UTC Actual Date and Time
	yyyy/mm/dd HH:MM
	Variable Value
	ISMN Quality Flag
	Data Provider Quality Flag, if existing


Network Information

	BFG_Nw
		Abstract: 
		Continent: Europe
		Country: Germany
		Stations: 1
		Status: running
		Data Range: from 1986-11-01 
		Type: project
		Url: 
		Reference: We acknowledge the work of Jens Wilhelmi in support of the ISMN;
		Variables: air temperature, precipitation, soil moisture, soil temperature, surface temperature, 
		Soil Moisture Depths: 0.25 - 0.25 m, 0.50 - 0.66 m, 0.85 - 0.85 m, 1.05 - 1.05 m
		Soil Moisture Sensors: SMT100, TRIME-ES P2, 

	BIEBRZA_S-1
		Abstract: Preparation of the method for determining biomass and soil moisture changes on the basis of data delivered by recent satellite missions
		Continent: Europe
		Country: Poland
		Stations: 30
		Status: running
		Data Range: from 2015-09-15 
		Type: project
		Url: http://www.igik.edu.pl/en
		Reference: Dabrowska-Zielinska K., Musial J., Malinska A., Budzynska M., Gurdak R., Kiryla W., Bartold M., Grzybowski P., (2018), Soil Moisture in the Biebrza Wetlands Retrieved from Sentinel-1 Imagery. Remote Sensing 2018, Vol. 
10(12), 1979. https://doi.org/10.3390/rs10121979;

Musial, J. P., Dabrowska-Zielinska, K., Kiryla, W., Oleszczuk, R., Gnatowski, T. & Jaszczynski, J. (2016), ‘Derivation and validation of the high resolution satellite soil moisture products: a case study of the biebrza sentinel-1 validation sites’, Geoinformation Issues 8(1 (8)), 37–53. https://doi.org/10.34867/gi.2016.4;
		Variables: precipitation, soil temperature, soil moisture, air temperature, 
		Soil Moisture Depths: 0.05 - 0.05 m, 0.10 - 0.10 m, 0.20 - 0.20 m, 0.50 - 0.50 m
		Soil Moisture Sensors: GS-3, 

	CALABRIA
		Abstract: 
		Continent: Europe
		Country: Italy
		Stations: 5
		Status: running
		Data Range: from 2000-01-01 
		Type: meteo
		Url: http://www.cfd.calabria.it/
		Reference: Brocca, L., Hasenauer, S., Lacava, T., Melone, F., Moramarco, T., Wagner, W., A, D., Matgen, P., Mart´ınez-Fern´andez, J., Llorens, P., Latron, J., Martin, C. & Bittelli, M. (2011), ‘Soil moisture estimation through ascat and amsr-e sensors: An intercomparison and validation study across europe’, Remote Sensing of Environment 115, 3390–3408. https://doi.org/10.1016/j.rse.2011.08.003;
		Variables: air temperature, precipitation, soil moisture, 
		Soil Moisture Depths: 0.30 - 0.30 m, 0.60 - 0.60 m, 0.90 - 0.90 m
		Soil Moisture Sensors: ThetaProbe ML2X, 

	CAMPANIA
		Abstract: This italian data set consists of two stations located near to the city of Naples in the south of Italy. It is managed by the "Centro Funzionale per la Previsione Meteorologica e il Monitoraggio Meteo-Pluvio-Idrometrico e delle Frane". The ISMN contains data from the operational start in 2000 until the end of 2008. The data sets include soil moisture measured at a depth of 0.30 m, precipitation, and air temperature.
		Continent: Europe
		Country: Italy
		Stations: 2
		Status: inactive
		Data Range: from 2000-11-26  to 2008-12-31
		Type: project
		Url: http://www.regione.campania.it/
		Reference: Brocca, L., Hasenauer, S., Lacava, T., Melone, F., Moramarco, T., Wagner, W., A, D., Matgen, P., Mart´ınez-Fern´andez, J., Llorens, P., Latron, J., Martin, C. & Bittelli, M. (2011), ‘Soil moisture estimation through ascat and amsr-e sensors: An intercomparison and validation study across europe’, Remote Sensing of Environment 115, 3390–3408. https://doi.org/10.1016/j.rse.2011.08.003;
		Variables: air temperature, precipitation, soil moisture, 
		Soil Moisture Depths: 0.30 - 0.30 m
		Soil Moisture Sensors: ThetaProbe ML2X, 

	COSMOS
		Abstract: A new project to measure soil moisture using a cosmic-ray technique. Currently, there are 67 stations deployed in 7 countries, which 59 are in USA, 1 in Germany, 1 in Switzerland, 1 in France, 1 in Brasil, 2 in Kenya, 1 in United Kingdom and 1 in Mexico.
		Continent: Americas
		Country: USA
		Stations: 109
		Status: running
		Data Range: from 2008-04-28 
		Type: project
		Url: http://cosmos.hwr.arizona.edu/
		Reference: Zreda M., Desilets D., Ferré Ty P.A., Scott R.L., “Measuring soil moisture content non-invasively at intermediate spatial scale using cosmic-ray neutrons”, Geophysical Research Letters 35(21), 2008. https://doi.org/10.1029/2008GL035655;

Zreda, M., W.J. Shuttleworth, X. Zeng, C. Zweck, D. Desilets, T. Franz, and R. Rosolem, 2012. COSMOS: the COsmic-ray Soil Moisture Observing System. Hydrology and Earth System Sciences 16, 4079-4099, https://doi.org/10.5194/hess-16-4079-2012;
		Variables: soil moisture, 
		Soil Moisture Depths: 0.00 - 0.04 m, 0.00 - 0.05 m, 0.00 - 0.06 m, 0.00 - 0.07 m, 0.00 - 0.08 m, 0.00 - 0.09 m, 0.00 - 0.10 m, 0.00 - 0.11 m, 0.00 - 0.12 m, 0.00 - 0.13 m, 0.00 - 0.14 m, 0.00 - 0.15 m, 0.00 - 0.16 m, 0.00 - 0.17 m, 0.00 - 0.18 m, 0.00 - 0.19 m, 0.00 - 0.20 m, 0.00 - 0.21 m, 0.00 - 0.22 m, 0.00 - 0.23 m, 0.00 - 0.24 m, 0.00 - 0.25 m, 0.00 - 0.26 m, 0.00 - 0.27 m, 0.00 - 0.28 m, 0.00 - 0.29 m, 0.00 - 0.30 m, 0.00 - 0.31 m, 0.00 - 0.32 m, 0.00 - 0.33 m, 0.00 - 0.34 m, 0.00 - 0.36 m, 0.00 - 0.37 m, 0.00 - 0.38 m, 0.00 - 0.39 m, 0.00 - 0.40 m, 0.00 - 0.41 m, 0.00 - 0.44 m, 0.00 - 0.55 m, 0.00 - 0.69 m, 0.00 - 0.90 m
		Soil Moisture Sensors: Cosmic-ray Probe, 

	COSMOS-UK
		Abstract: The COSMOS-UK network is established and operated by the UK Centre for Ecology and Hydrology (UKCEH). It is the first network to systematically measure soil moisture throughout the UK, and represents a range of climate, soils and vegetation. The network consists of ~50 sites, each recording a number of hydrometeorological and soil variables. Each site hosts a cosmic-ray neutron sensor (CRNS); a novel sensor technology which counts fast neutrons in the surrounding atmosphere. In combination with the recorded hydrometeorological data, neutron counts are used to derive Volumetric Water Content (VWC) over a field scale (~0.1 km2) (COSMOS VWC), at daily resolution. Alongside the CRNS, each site hosts several point soil moisture probes recording at 30 minute resolution. More information is available from the COSMOS-UK website: https://cosmos.ceh.ac.uk/ . The full dataset, along with quality flags, is available at: https://doi.org/10.5285/5060cc27-0b5b-471b-86eb-71f96da0c80f .


************************************************************************************************************
IMPORTANT NOTE: The Cosmic-ray neutron sensor (CRNS) is placed just above the ground and counts the naturally occurring neutrons (originating from cosmic rays). The neutrons are scattered by hydrogen atoms, which are present primarily in the soil water. The CRNS neutron count rate (after corrections) reduces with increasing soil moisture content, and can therefore be used, via a calibration curve, to infer the soil Volumetric Water Content (VWC). The CRNS counts neutrons which may have been scattered many times, such that they may have interacted with the ground soil moisture over distances of more than 200 m from the probe, and from tens centimetres of soil depth. This local scattering of neutrons determines the horizontal and vertical footprint of the sensor, or the measurement support volume, and yields the important characteristic of averaging the soil moisture measurement over a large area. Using neutron scattering models, the typical footprint is determined (~12 hectares), although there is some dependence on the VWC, particularly for the soil depth of measurement. For this reason, the CRNS depth of measurement is given as an average for the time series and location, but it should be appreciated that actual sensing depth will be reduced in wet conditions, compared with dry conditions (from around 10 cm to 30 cm depth respectively).
************************************************************************************************************

		Continent: Europe
		Country: UK
		Stations: 49
		Status: running
		Data Range: from 2013-10-01 
		Type: project
		Url: https://cosmos.ceh.ac.uk/
		Reference: Cooper, H. M., Bennett, E., Blake, J., Blyth, E., Boorman, D., Cooper, E., Evans, J., Fry, M., Jenkins, A., Morrison, R., Rylett, D., Stanley, S., Szczykulska, M., Trill, E., Antoniou, V., Askquith-Ellis, A., Ball, L., Brooks, M., Clarke, M. A., Cowan, N., Cumming, A., Farrand, P., Hitt, O., Lord, W., Scarlett, P., Swain, O., Thornton, J., Warwick, A., and Winterbourn, B.: COSMOS-UK: national soil moisture and hydrometeorology data for environmental science research, Earth Syst. Sci. Data, 13, 1737–1757, https://doi.org/10.5194/essd-13-1737-2021, 2021.
		Variables: precipitation, soil temperature, air temperature, soil moisture, snow depth, 
		Soil Moisture Depths: 0.00 - 0.30 m, 0.05 - 0.05 m, 0.10 - 0.10 m, 0.15 - 0.15 m, 0.25 - 0.25 m, 0.50 - 0.50 m
		Soil Moisture Sensors: Cosmic-ray Probe, TDT, 

	FMI
		Abstract: The finnish network "FMI" includes one station that contains multiple soil moisture measurements in 2cm and 10cm depth, taken only a few meters next to each other. Additionaly air temperature is measured in 2m height and soil temperature in 2cm depth. The datasets start at 2007-01-25 and are updated once a day. The FMI is the first network that has been implemented with data updates in Near Real Time.
		Continent: Europe
		Country: Finland
		Stations: 27
		Status: running
		Data Range: from 2007-01-25 
		Type: project
		Url: http://fmiarc.fmi.fi/
		Reference: Ikonen, J., Smolander, T., Rautiainen, K., Cohen, J., Lemmetyinen, J., Salminen, M. & Pulliainen, J. (2018), ‘Spatially distributed evaluation of esa cci soil moisture products in a northern boreal forest environment’, Geosciences 8(2), 51., https://doi.org/10.3390/geosciences8020051;

Ikonen, J., Vehviläinen, J., Rautiainen, K., Smolander, T., Lemmetyinen, J., Bircher, S. & Pulliainen, J. (2015), ‘The sodankylä in-situ soil moisture observation network: an example application to earth observation data product evaluation’, GID 5(2), 599–629., https://doi.org/10.5194/gi-5-95-2016;
		Variables: soil temperature, air temperature, soil moisture, 
		Soil Moisture Depths: 0.02 - 0.02 m, 0.05 - 0.05 m, 0.10 - 0.10 m, 0.20 - 0.20 m, 0.40 - 0.40 m, 0.60 - 0.60 m, 0.80 - 0.80 m
		Soil Moisture Sensors: 5TE, CS655, ThetaProbe ML2X, 

	FR_Aqui
		Abstract: The Fr_Aqui network is located in France and hosted by the Institue of Agricultural Research (INRA); it consists of 5 stations with soil moisture and soil temperature measurements in 6 different  depths.
		Continent: Europe
		Country: France
		Stations: 5
		Status: running
		Data Range: from 2010-01-01 
		Type: meteo
		Url: 
		Reference: Al-Yaari, A., Dayau, S., Chipeaux, C., Aluome, C., Kruszewski, A., Loustau, D. & Wigneron, J.-P. (2018), ‘The aqui soil moisture network for satellite microwave remote sensing validation in south-western france’, Remote Sensing 10(11), https://doi.org/10.3390/rs10111839;

Wigneron, J.-P., Dayan, S., Kruszewski, A., Aluome, C., Al-Yaari, A., Fan, L., Guven, S., Chipeaux, C., Moisy, C., Guyon, D. & Loustau, D. (2018), The aqui network: Soil moisture sites in the “les landes” forest and graves vineyards (bordeaux aquitaine region, france), pp. 3739–3742., https://doi.org/10.1109/IGARSS.2018.8517392;
		Variables: soil moisture, soil temperature, 
		Soil Moisture Depths: 0.01 - 0.01 m, 0.03 - 0.03 m, 0.05 - 0.05 m, 0.10 - 0.10 m, 0.15 - 0.15 m, 0.20 - 0.20 m, 0.21 - 0.21 m, 0.25 - 0.25 m, 0.30 - 0.30 m, 0.34 - 0.34 m, 0.45 - 0.45 m, 0.50 - 0.50 m, 0.55 - 0.55 m, 0.56 - 0.56 m, 0.70 - 0.70 m, 0.80 - 0.80 m, 0.90 - 0.90 m
		Soil Moisture Sensors: ThetaProbe ML2X, 

	GROW
		Abstract: The GROW Observatory (GROW) is a European-wide project engaging thousands of growers, scientists and others passionate about the land. We will discover together, using simple tools to better manage soil and grow food, while contributing to vital scientific environmental monitoring.
		Continent: Europe
		Country: UK
		Stations: 151
		Status: inactive
		Data Range: from 2016-11-01  to 2019-10-31
		Type: project
		Url: https://growobservatory.org/index.html
		Reference: Xaver, A., Zappa, L., Rab, G., Pfeil, I., Vreugdenhil, M., Hemment, D. & Dorigo, W. A. (2020), ‘Evaluating the suitability of the consumer low-cost parrot ﬂower power soil moisture sensor for scientiﬁc environmental applications’, Geoscientiﬁc Instrumentation, Methods and Data Systems 9(1), 117–139., https://doi.org/10.5194/gi-9-117-2020;

Zappa, L., Woods, M., Hemment, D., Xaver, A. & Dorigo, W. (2020), Evaluation of remotely sensed soil moisture products using crowdsourced measurements, Eighth International Conference on Remote Sensing and Geoinformation of Environment, SPIE, Cyprus., https://doi.org/;

Zappa, L., Forkel, M., Xaver, A. & Dorigo, W. (2019), ‘Deriving ﬁeld scale soil moisture from satellite observations and ground measurements in a hilly agricultural region’, Remote Sensing 11(22), 2596., https://doi.org/10.3390/rs11222596, https://doi.org/10.1117/12.2571913;
		Variables: air temperature, soil moisture, 
		Soil Moisture Depths: 0.00 - 0.10 m
		Soil Moisture Sensors: Flower Power, 

	GTK
		Abstract: Geological Survey of Finland
		Continent: Europe
		Country: Finland
		Stations: 7
		Status: running
		Data Range: from 2001-03-01 
		Type: project
		Url: https://www.gtk.fi/en/
		Reference: We acknowledge the work of Raimo Sutinen and the GTK team in support of the ISMN;
		Variables: air temperature, soil moisture, soil temperature, 
		Soil Moisture Depths: 0.10 - 0.10 m, 0.30 - 0.30 m, 0.50 - 0.50 m, 0.70 - 0.70 m, 0.90 - 0.90 m
		Soil Moisture Sensors: CS615, CS616, 

	HOAL
		Abstract: 
		Continent: Europe
		Country: Austria
		Stations: 33
		Status: running
		Data Range: from 2013-12-07 
		Type: research network

		Url: https://hoal.hydrology.at/research/soil-moisture

		Reference: Blöschl, Günter, et al. "The hydrological open air laboratory (HOAL) in Petzenkirchen: A hypothesis-driven observatory." Hydrology and Earth System Sciences 20.1 (2016): 227-255., https://doi.org/10.5194/hess-20-227-2016;

M. Vreugdenhil et al., "Towards a high-density soil moisture network for the validation of SMAP in Petzenkirchen, Austria," 2013 IEEE International Geoscience and Remote Sensing Symposium - IGARSS, Melbourne, VIC, 2013, pp. 1865-1868, https://doi.org/10.1109/IGARSS.2013.6723166.;
		Variables: soil temperature, soil moisture, 
		Soil Moisture Depths: 0.05 - 0.05 m, 0.10 - 0.10 m, 0.20 - 0.20 m, 0.50 - 0.50 m, 1.00 - 1.00 m
		Soil Moisture Sensors: SPADE Time Domain Transmissivity, 

	HOBE
		Abstract: Soil moisture and soil temperature network with 30 stations within the area of major signal contribution of one selected SMOS grid node in the Skjern River Catchment
		Continent: Europe
		Country: Denmark
		Stations: 32
		Status: inactive
		Data Range: from 2009-09-08  to 2019-03-13
		Type: project
		Url: http://www.hobe.dk/
		Reference: Jensen, K. & Refsgaard, J. (2018), ‘Hobe: The danish hydrological observatory’, Vadose Zone Journal 17., https://doi.org/10.2136/vzj2018.03.0059;

Bircher, S., Skou, N., Jensen, K., Walker, J. & Rasmussen, L. (2012), ‘A soil moisture and temperature network for smos validation in western denmark’, Hydrology and Earth System Sciences 16., https://doi.org/10.5194/hess-16-1445-2012;
		Variables: soil temperature, soil moisture, 
		Soil Moisture Depths: 0.00 - 0.05 m, 0.20 - 0.25 m, 0.50 - 0.55 m
		Soil Moisture Sensors: Decagon 5TE, 

	HYDROL-NET_PERUGIA
		Abstract: This network has 1 station called WEEF (Water Engineering Experimental Field) near the city of Perugia, Central Italy. It provides of measurements of soil moisture at 4 different depths, soil temperature at 2 depths, precipitation, and air temperature. It is operated by the Department of Civil and Environmental Engineering of the University of Perugia since the beginning of 2010.
		Continent: Europe
		Country: Italy
		Stations: 2
		Status: running
		Data Range: from 2010-01-01 
		Type: project
		Url: http://www.ing1.unipg.it/
		Reference: FLAMMINI A., MORBIDELLI R., SALTALIPPI C., PICCIAFUOCO T., CORRADINI C., GOVINDARAJU R.S. “Reassessment of a semi-analytical field-scale infiltration model through experiments under natural rainfall events”, Journal of Hydrology, 565, 835-845, 2018, Codice Scopus: 2-s2.0-85053026749, Codice WOS: 000447477200069, https://doi.org/10.1016/j.jhydrol.2018.08.073;

FLAMMINI A., CORRADINI C., MORBIDELLI R., SALTALIPPI C., PICCIAFUOCO T., GIRALDEZ J.V. “Experimental Analyses of the Evaporation Dynamics in Bare Soils under Natural Conditions”, Water Resources Management, 32 (3), 1153-1166, 2018, Codice Scopus: 2-s2.0-85034632795, Codice WOS: 000422982300020, https://doi.org/10.1007/s11269-017-1860-x;

Morbidelli, R., Saltalippi, C., Flammini, A., Cifrodelli, M., Picciafuoco, T., Corradini, C. & Govindaraju, R. S. (2017), ‘In situ measurements of soil saturated hydraulic conductivity: Assessment of reliability through rainfall–runoﬀ experiments’, Hydrological Processes 31(17), 3084–3094, https://doi.org/10.1002/hyp.11247;

MORBIDELLI R., SALTALIPPI C., FLAMMINI A., ROSSI E., CORRADINI C., “Soil water content vertical profiles under natural conditions: matching of experiments and simulations by a conceptual model”, Hydrological Processes, 28 (17), 4732-4742, 2014, Codice Scopus: 2-s2.0-84905732846, Codice WOS: 000340611500006, https://doi.org/10.1002/hyp.9973;

MORBIDELLI R., CORRADINI C., SALTALIPPI C., FLAMMINI A., ROSSI E., “Infiltration-soil moisture redistribution under natural conditions: experimental evidence as a guideline for realizing simulation models”, Hydrology and Earth System Sciences, 15, 2937-3945, 2011, Codice Scopus: 2-s2.0-80052885350, Codice WOS: 000295357100012, https://doi.org/10.5194/hess-15-2937-2011;
		Variables: air temperature, precipitation, soil moisture, soil temperature, 
		Soil Moisture Depths: 0.05 - 0.05 m, 0.15 - 0.15 m, 0.25 - 0.25 m, 0.35 - 0.35 m
		Soil Moisture Sensors: TDR-Soil Moisture Equipment Corp. TRASE-BE, 

	IMA_CAN1
		Abstract: Soil Moisture Network installed in three vineyard plots, with different inter-rows soil management. The plots are also monitored for runoff and soil erosion.Weather data available from a station near the plots.
		Continent: Europe
		Country: Italy
		Stations: 12
		Status: inactive
		Data Range: from 2011-08-23  to 2015-10-23
		Type: campaign
		Url: http://sustag.imamoter.cnr.it/index.php/cannona-db
		Reference: Capello, G., Biddoccu, M., Ferraris, S. & Cavallo, E. (2019), ‘Effects of tractor passes on hydrological and soil erosion processes in tilled and grassed vineyards’, Water 11(10), 2118., https://doi.org/10.3390/w11102118;

Raffelli, G., Id, M., Previati, M., Id, D., Canone, D., Gisolo, D., Bevilacqua, I., Capello, G., Biddoccu, M., Cavallo, E., Id, R., Deiana, R., Id, G., Cassiani, G. & Ferraris, S. (2018), ‘Local-and plot-scale measurements of soil moisture: Time and spatially resolved ﬁeld techniques in plain, hill and mountain sites’, Water 9., https://doi.org/10.3390/w9090706;

Marcella Biddoccu, Stefano Ferraris, Francesca Opsi, Eugenio Cavallo. Long-term monitoring of soil management effects on runoff and soil erosion in sloping vineyards in Alto Monferrato (North–West Italy). Soil and Tillage Research, Volume 155, 2016, Pages 176-189, ISSN 0167-1987, https://doi.org/10.1016/j.still.2015.07.005.;
		Variables: soil moisture, soil temperature, 
		Soil Moisture Depths: 0.10 - 0.10 m
		Soil Moisture Sensors: 5TM, 

	IPE
		Abstract: 
		Continent: Europe
		Country: Spain
		Stations: 2
		Status: running
		Data Range: from 2008-04-03 
		Type: meteo
		Url: 
		Reference: Alday, J. G., Camarero, J. J., Revilla, J. & Dios, V. R. (2020), ‘Similar diurnal, seasonal and annual rhythms in radial root expansion across two coexisting mediterranean oak species’, Tree Physiology, https://doi.org/10.1093/treephys/tpaa041;
		Variables: air temperature, precipitation, soil moisture, soil temperature, 
		Soil Moisture Depths: 0.00 - 0.06 m, 0.00 - 0.30 m, 0.10 - 0.10 m
		Soil Moisture Sensors: CS616, CS650, ThetaProbe ML2X, 

	LABFLUX
		Abstract: The Lab performs research, tutorial ad dissemination regarding measurements and modeling of water and moisture fluxes in the natural, agricultural and built environments. Main focus is on porous media like soil, snow and wood. Specifically addressed are the monitoring of : meteorological variables, energy fluxes, soil-plant-atmosphere interactions, water dynamics, and hillslope processes.
		Continent: Europe
		Country: Italy
		Stations: 4
		Status: running
		Data Range: from 2012-01-01 
		Type: project
		Url: https://www.dist.polito.it/il_dipartimento/laboratori/labflux
		Reference: We acknowledge the work of Davide Gisolo, Canone Davide, Ferrari Stefano, Alessio Gentile and Previati Maurizio as well as the LABFLUX network team in support of the ISMN;

		Variables: air temperature, precipitation, soil moisture, soil temperature, 
		Soil Moisture Depths: 0.10 - 0.10 m, 0.20 - 0.20 m, 0.40 - 0.40 m
		Soil Moisture Sensors: CS616, Meter EC-5, 

	METEROBS
		Abstract: 
		Continent: Europe
		Country: Italy
		Stations: 1
		Status: inactive
		Data Range: from 1986-01-01 
		Type: project
		Url: http://mistrals.sedoo.fr/HyMeX/Plateform-search?datsId=532
		Reference: We acknowledge the work of Nazzareno Diodato and the METEROBS team in support of the ISMN;
		Variables: soil moisture, 
		Soil Moisture Depths: 0.10 - 0.10 m, 0.20 - 0.20 m, 0.30 - 0.30 m, 0.40 - 0.40 m, 0.50 - 0.50 m
		Soil Moisture Sensors: EnviroSCAN, 

	MOL-RAO
		Abstract: This network is operated from the German Meteorological Service and consists of two stations. While the Station Falkenberg has a grass type vegetation, Kehrigk is situated in a pine forest. Volumetric soil moisture, soil temperature, air temperature and precipitation are provied for the period from 2003 to 2008. 
		Continent: Europe
		Country: Germany
		Stations: 2
		Status: running
		Data Range: from 2003-01-01 
		Type: project
		Url: http://www.dwd.de/mol
		Reference: Site and Data Report for the Lindenberg Reference Site in CEOP - Phase 1, Berichte des Deutschen Wetterdienstes, 230, Offenbach am Main;
		Variables: air temperature, precipitation, soil moisture, soil temperature, 
		Soil Moisture Depths: 0.08 - 0.08 m, 0.10 - 0.10 m, 0.15 - 0.15 m, 0.20 - 0.20 m, 0.30 - 0.30 m, 0.45 - 0.45 m, 0.60 - 0.60 m, 0.90 - 0.90 m, 1.50 - 1.50 m
		Soil Moisture Sensors: TRIME-EZ, 

	NVE
		Abstract: Ground water and soil moisture network

		Continent: Europe
		Country: Norway
		Stations: 6
		Status: running
		Data Range: from 1989-06-15 
		Type: permanent

		Url: https://www.nve.no/hydrology/?ref=mainmenu
		Reference: We acknowledge the work of Fred Wenger and the Norwegian water resources and energy direcorate (NVE) team in support of the ISMN;
		Variables: air temperature, precipitation, soil moisture, soil temperature, 
		Soil Moisture Depths: 0.10 - 0.10 m, 0.20 - 0.20 m, 0.30 - 0.30 m, 0.40 - 0.40 m, 0.60 - 0.60 m, 1.00 - 1.00 m
		Soil Moisture Sensors: Decagon 5 TM, Delta-T, Sutron, 

	ORACLE
		Abstract: 
		Continent: Europe
		Country: France
		Stations: 6
		Status: running
		Data Range: from 1985-10-18 
		Type: project
		Url: http://gisoracle.irstea.fr/?lang=en;https://bdoh.irstea.fr/ORACLE/
		Reference: We acknowledge the work of Arnaud Blanchouin and ORACLE team of the Institut national de recherche en sciences et technologies pour l"environment et l"agriculture, France in support of the ISMN;
		Variables: air temperature, precipitation, soil moisture, soil temperature, 
		Soil Moisture Depths: 0.03 - 0.03 m, 0.05 - 0.05 m, 0.06 - 0.06 m, 0.10 - 0.10 m, 0.15 - 0.15 m, 0.20 - 0.20 m, 0.25 - 0.25 m, 0.30 - 0.30 m, 0.35 - 0.35 m, 0.40 - 0.40 m, 0.45 - 0.45 m, 0.50 - 0.50 m, 0.55 - 0.55 m, 0.65 - 0.65 m, 0.70 - 0.70 m, 0.75 - 0.75 m, 0.85 - 0.85 m, 0.90 - 0.90 m, 0.95 - 0.95 m, 1.05 - 1.05 m, 1.10 - 1.10 m, 1.15 - 1.15 m, 1.30 - 1.30 m, 1.35 - 1.35 m, 1.50 - 1.50 m, 1.55 - 1.55 m
		Soil Moisture Sensors: Solo 40, ThetaProbe ML2X, TRASE 16, 

	REMEDHUS
		Abstract: 
		Continent: Europe
		Country: Spain
		Stations: 24
		Status: running
		Data Range: from 2005-01-01 
		Type: project
		Url: http://campus.usal.es/~hidrus/
		Reference: Gonzalez-Zamora, A., Sanchez, N., Pablos, M. & Martinez-Fernandez, J. (2018), ‘Cci soil moisture assessment with smos soil moisture and in situ data under different environmental conditions and spatial scales in spain’, Remote Sensing of Environment 225, https://doi.org/10.1016/j.rse.2018.02.010;
		Variables: soil moisture, soil temperature, 
		Soil Moisture Depths: 0.00 - 0.05 m
		Soil Moisture Sensors: Stevens Hydra Probe, 

	RSMN
		Abstract: The project proposal aims at paving the way for the utilisation of satellite derived soil moisture products in Romania, creating the framework for the validation and evaluation of actual & future satellite microwave soil moisture derived products, demonstrating its value, and by developing the necessary expertise for successfuly approaching implementations in the Societal Benefit Areas (as they were defined in GEOSS)

		Continent: Europe
		Country: Romania
		Stations: 20
		Status: running
		Data Range: from 2014-04-09 
		Type: meteo
		Url: http://assimo.meteoromania.ro
		Reference: We acknowledge the work of Andrei Diamandi and Adelina Mihai and the Romanian National Meteorological Administration team in support of the ISMN;
		Variables: air temperature, precipitation, soil moisture, soil temperature, 
		Soil Moisture Depths: 0.00 - 0.05 m
		Soil Moisture Sensors: 5TM, 

	RU-ADDFerti
		Abstract: 
		Continent: Europe
		Country: Germany
		Stations: 30
		Status: running
		Data Range: from 2023-06-01 
		Type: project
		Url: 
		Reference: We acknowledge the work of Alexander Steiger and the RU-ADDFerti network team in support of the ISMN;
		Variables: soil moisture, soil temperature, 
		Soil Moisture Depths: 0.25 - 0.25 m, 0.50 - 0.50 m
		Soil Moisture Sensors: LSE01, 

	Ru_CFR
		Abstract: 
		Continent: Europe
		Country: Russia
		Stations: 2
		Status: running
		Data Range: from 2015-05-25 
		Type: fluxnet
		Url: 
		Reference: We acknowledge the work of Andrej Varlagin and Adelina Mihai and the Ru_CFR team of the A.N. Severtsov Institute of Ecology and Evolution, Russian Academy of Sciences team in support of the ISMN;

		Variables: air temperature, precipitation, soil moisture, soil temperature, 
		Soil Moisture Depths: 0.05 - 0.05 m, 0.15 - 0.15 m, 0.50 - 0.50 m, 0.80 - 0.80 m, 1.00 - 1.00 m
		Soil Moisture Sensors: Hydraprobe II, 

	SMOSMANIA
		Abstract: 
		Continent: Europe
		Country: France
		Stations: 22
		Status: running
		Data Range: from 2003-01-01 
		Type: project
		Url: http://www.hymex.org
		Reference: Calvet, J.-C., Fritz, N., Berne, C., Piguet, B., Maurel, W. & Meurey, C. (2016), ‘Deriving pedotransfer functions for soil quartz fraction in southern france from reverse modeling’, SOIL 2(4), 615–629, https://doi.org/10.5194/soil-2-615-2016;

Albergel, C., Rüdiger, C., Pellarin, T., Calvet, J.-C., Fritz, N., Froissard, F., Suquia, D., Petitpa, A., Piguet, B., and Martin, E.: From near-surface to
root-zone soil moisture using an exponential filter: an assessment of the method based
on insitu observations and model simulations, Hydrol. Earth Syst. Sci., 12, 1323–1337, 2008, https://doi.org/10.5194/hess-12-1323-2008;

Calvet, J.-C., Fritz, N., Froissard, F., Suquia, D., Petitpa, A., and Piguet, B.: In situ soil moisture observations for the CAL/VAL of SMOS: the SMOSMANIA network, International Geoscience and Remote Sensing Symposium, IGARSS, Barcelona, Spain, 23-28 July 2007, 1196-1199, https://doi.org/10.1109/IGARSS.2007.4423019, 2007.;
		Variables: soil moisture, soil temperature, 
		Soil Moisture Depths: 0.05 - 0.05 m, 0.10 - 0.10 m, 0.20 - 0.20 m, 0.30 - 0.30 m
		Soil Moisture Sensors: ThetaProbe ML2X, ThetaProbe ML3, 

	STEMS
		Abstract: Soil Moisture Network installed in rainfed vineyard plots, with different inter-rows soil management. The plots are also monitored for runoff and soil erosion. Weather data available from a station near the plots.
		Continent: Europe
		Country: Italy
		Stations: 4
		Status: running
		Data Range: from 2015-12-04 
		Type: campaign
		Url: https://sustag.to.cnr.it/index.php/cannona-db
		Reference: Darouich, H., Ramos, T.B., Pereira, L.S., Rabino, D., Bagagiolo, G., Capello, G., Simionesei, L., Cavallo, E., Biddoccu, M. Water Use and Soil Water Balance of Mediterranean Vineyards under Rainfed and Drip Irrigation Management: Evapotranspiration Partition and Soil Management Modelling for Resource Conservation. Water 2022, 14, 554. https://doi.org/10.3390/w14040554;

Capello G, Biddoccu M, Ferraris S, Cavallo E, 2019. Effects of tractor passes on hydrological and soil erosion processes in tilled and grassed vineyards. Water 2019, 11(10), 2118, https://doi.org/10.3390/w11102118;
		Variables: air temperature, precipitation, soil moisture, soil temperature, 
		Soil Moisture Depths: 0.10 - 0.10 m, 0.20 - 0.20 m, 0.30 - 0.30 m, 0.40 - 0.40 m, 0.50 - 0.50 m
		Soil Moisture Sensors: 5TM, EC5, 

	SWEX_POLAND
		Abstract: 
		Continent: Europe
		Country: Poland
		Stations: 6
		Status: inactive
		Data Range: from 2006-08-03  to 2013-05-06
		Type: project
		Url: 
		Reference: W. Marczewski, J. Slominski, E. Slominska, B. Usowicz, J. Usowicz, S. Romanov, O. Maryskevych, J. Nastula, and J. Zawadzki, 2010: Strategies for validating and directions for employing SMOS data, in the Cal-Val project SWEX (3275) for wetlands, Hydrol. Earth Syst. Sci. Discuss., 7, 7007–7057, https://doi.org/10.5194/hessd-7-7007-2010;
		Variables: precipitation, soil moisture, soil temperature, 
		Soil Moisture Depths: 0.00 - 0.02 m, 0.05 - 0.05 m, 0.10 - 0.10 m, 0.20 - 0.20 m, 0.30 - 0.30 m, 0.40 - 0.40 m, 0.50 - 0.50 m, 0.60 - 0.60 m, 0.60 - 1.00 m, 1.00 - 1.00 m
		Soil Moisture Sensors: D-LOG-mpts, PR2 - Profile Probe, 

	TERENO
		Abstract: Soil moisture network in Germany, There are 4 observatories: in Northeastern Germany- Lowlan Observatory coordinated by German Research Centre of Geosciences, in Harz/Central Germany-  Lowland Observatory coordinated by Helmholtz Centre for Environmental Research, in Eifel/Lower Rhine Valley- Observatory coordinated by Research Centre Juelich and in Bavarian Alps/pre-Alps- Obervatory coordinated by Karlsruhe Institute of Technology and German Center for Environmental Health
		Continent: Europe
		Country: Germany
		Stations: 5
		Status: running
Data Range: 

		Type: meteo
		Url: https://www.tereno.net/joomla/index.php/overview
		Reference: Bogena, H.R., Montzka, C., Huisman, J.A., Graf, A., Schmidt, M., Stockinger, M., Von Hebel, C., Hendricks-Franssen, H.J., Van der Kruk, J., Tappe, W. and Lücke, A., 2018. The TERENO‐Rur hydrological observatory: A multiscale multi‐compartment research platform for the advancement of hydrological science. Vadose Zone Journal, 17(1), pp.1-22, https://doi.org/10.2136/vzj2018.03.0055;

Bogena, H. R. (2016), ‘Tereno: German network of terrestrial environmental observatories’, Journal of large-scale research facilities JLSRF 2, 52, http://dx.doi.org/10.17815/jlsrf-2-98;

Bogena, H., Kunkel, R., Puetz, T., Vereecken, H., Krueger, E., Zacharias, S., Dietrich, P., Wollschlaeger, U., Kunstmann, H., Papen, H. and Schmid, H.P., 2012. Tereno-long-term monitoring network for terrestrial environmental research. Hydrologie und Wasserbewirtschaftung, 56(3), pp.138-143, https://doi.org/DOI:%10.5675;

Zacharias, S., H.R. Bogena, L. Samaniego, M. Mauder, R. Fuß, T. Pütz, M. Frenzel, M. Schwank, C. Baessler, K. Butterbach-Bahl, O. Bens, E. Borg, A. Brauer, P. Dietrich, I. Hajnsek, G. Helle, R. Kiese, H. Kunstmann, S. Klotz, J.C. Munch, H. Papen, E. Priesack, H. P. Schmid, R. Steinbrecher, U. Rosenbaum, G. Teutsch, H. Vereecken. 2011. A Network of Terrestrial Environmental Observatories in Germany. Vadose Zone J. 10. 955–973, https://doi.org/10.2136/vzj2010.0139;
		Variables: air temperature, precipitation, soil moisture, soil temperature, 
		Soil Moisture Depths: 0.05 - 0.05 m, 0.20 - 0.20 m, 0.50 - 0.50 m
		Soil Moisture Sensors: Hydraprobe II Sdi-12, 

	TWENTE
		Abstract: The Twente region in the east of the Netherlands hold a network that monitors since 2009 profile soil moisture and temperature at twenty locations mostly in the rural environment. In addition, intensive measurement campaigns have been performed in 2009, 2015, 2016, and 2017 at number of measurement locations as a part of MSc and PhD research. The development of the network infrastructure has been supported through various EU and NWO-funded projects, and forthcoming data has been successfully used for the validation of satellite derived surface soil moisture products. The early development of the network has been described in Dente et al. (2011), but over the years the design of the network has altered considerably with the most recent updates documented in Van der Velde et al. (2021). In 2019, the Twente network has been operational for more than a decade and with this deposit we would like to make this data freely and well documented available for use by the science and professional communities. An accompanying data paper is under development and will be submitted to Earth System Science Data journal, which provide additional background information.
		Continent: Europe
		Country: Netherlands
		Stations: 44
		Status: running
		Data Range: from 2009-01-01 
		Type: project
		Url: https://doi.org/10.5194/essd-15-1889-2023
		Reference: Van der Velde, R., Benninga, H. J. F., Retsios, B., Vermunt, P. C., & Salama, M. S. (2023). Twelve years of profile soil moisture and temperature measurements in Twente, the Netherlands. Earth System Science Data, 15(4), 1889-1910.
https://doi.org/10.5194/essd-15-1889-2023
https://essd.copernicus.org/articles/15/1889/2023/

		Variables: soil temperature, soil moisture, 
		Soil Moisture Depths: 0.05 - 0.05 m, 0.10 - 0.10 m, 0.20 - 0.20 m, 0.40 - 0.40 m, 0.80 - 0.80 m
		Soil Moisture Sensors: 5TM, EC-TM, 

	UDC_SMOS
		Abstract: Soil moisture datasets of 11 stations near the city Munich in Germany are provided.  The measurements are taken at five different layers up to a depth of 40 cm. At some stations soil moisture of a specific layer is measured by multiple sensors. All stations of this network are situated on grassland. Meteorological data for the stations 5, 14, 16, 49, 74, 80, 115, 118 and 125 is available for free via the website of the Bavarian State Research Center for Agriculture (http://www.wetter-by.de/).
The soil moisture network is run in cooperation with the Bavarian State Research Center for Agriculture. This work is carried out as part of the project SMOSHYD (FKZ 50EE0731) funded by the German Aerospace Centre (DLR).
		Continent: Europe
		Country: Germany
		Stations: 11
		Status: inactive
		Data Range: from 2007-11-08  to 2011-10-21
		Type: project
		Url: http://www.geographie.uni-muenchen.de/department/fiona/forschung/projekte/index.php?projekt_id=103
		Reference: Schlenz, F., Dall’Amico, J., Loew, A., Mauser, W. (2012): Uncertainty Assessment of the SMOS Validation in the Upper Danube Catchment. IEEE Transactions on Geoscience and Remote Sensing, 50(5), pp.1517–1529, https://doi.org/10.1109/TGRS.2011.2171694;

A. Loew, J. T. Dall"Amico, F. Schlenz, W. Mauser (2009): The Upper Danube soil moisture validation site: measurements and activities, paper presented at Earth Observation and Water Cycle conference, Frascati (Rome), 18 - 20 November 2009, to be published in ESA Special dataation SP-674, https://ui.adsabs.harvard.edu/abs/2009ESASP.674E..56L;
		Variables: soil moisture, 
		Soil Moisture Depths: 0.00 - 0.10 m, 0.05 - 0.05 m, 0.10 - 0.10 m, 0.20 - 0.20 m, 0.40 - 0.40 m
		Soil Moisture Sensors: EC5, EC5 I, EC5 II, EC5 III, EC5 IV, EC5 V, EC5 VI, EC-ET, EC-ET 2, IMKO TDR, IMKO TDR 1, IMKO TDR 2, 

	UMBRIA
		Abstract: The soil moisture network of the Civil Protection Functional Centre (CFD Umbria), together with the Research Institute for Geo-Hydrological Protection and Consiglio Nazionale delle Ricerca (abbreviated CNR-IRPI)  is located near the city of Perugia at Lake Trasimeno in the middle of Italy and consists of 7 stations. Four of these seven stations come from the old Network CRN_IRPI which are now part of the UMBRIA Network. One station became operational in the year 2002 and is providing soil moisture measurements at 3 layers and additionaly precipitation and air temperature observations. Other 3 stations, became operational in the year 2007 collect soil moisture measurements at 3 depths. The observed variables are sampled each hour.
		Continent: Europe
		Country: Italy
		Stations: 13
		Status: running
		Data Range: from 2002-10-09 
		Type: project
		Url: http://www.cfumbria.it/; http://hydrology.irpi.cnr.it/
		Reference: Brocca, L., Hasenauer, S., Lacava, T., Melone, F., Moramarco, T., Wagner, W., Dorigo, W., Matgen, P., Martínez-Fernández, J., Llorens, P., Latron, J., Martin, C., Bittelli, M. (2011). Soil moisture estimation through ASCAT and AMSR-E sensors: an intercomparison and validation study across Europe. Remote Sensing of Environment, 115, 3390-3408, https://doi.org/10.1016/j.rse.2011.08.003;

Brocca, L., Melone, F., Moramarco, T., Morbidelli, R. (2009). Antecedent wetness conditions based on ERS scatterometer data. Journal of Hydrology, 364 (1-2), 73-87, https://doi.org/10.1016/j.jhydrol.2008.10.007;

Brocca, L., Melone, F., Moramarco, T. (2008). On the estimation of antecedent wetness condition in rainfall-runoff modelling. Hydrological Processes, 22 (5), 629-642, https://doi.org/10.1002/hyp.6629;
		Variables: air temperature, precipitation, soil moisture, 
		Soil Moisture Depths: 0.05 - 0.15 m, 0.15 - 0.25 m, 0.25 - 0.35 m, 0.35 - 0.45 m, 0.45 - 0.55 m
		Soil Moisture Sensors: EnviroSCAN, EnviroSMART, ThetaProbe ML2X, 

	UMSUOL
		Abstract: 
		Continent: Europe
		Country: Italy
		Stations: 1
		Status: running
		Data Range: from 2004-08-31 
		Type: project
		Url: http://www.arpa.emr.it/sim/
		Reference: We acknowledge the work of Andrea Pasquali and the UMSUOL network team provided by the Agenzia Regionale Prevenzione Ambiente - Servizio Idro-Meteo-Clima (ARPA - SIMC) in support of the ISMN;

		Variables: soil moisture, 
		Soil Moisture Depths: 0.10 - 0.10 m, 0.25 - 0.25 m, 0.45 - 0.45 m, 0.70 - 0.70 m, 1.00 - 1.00 m, 1.35 - 1.35 m, 1.80 - 1.80 m
		Soil Moisture Sensors: TDR 100, 

	VAS
		Abstract: Soil moisture network in Spain, University of Valencia, Climatology from Satellites Group and Jucar River Basin Authority
		Continent: Europe
		Country: Spain
		Stations: 3
		Status: running
		Data Range: from 2002-01-01 
		Type: meteo
		Url: http://nimbus.uv.es/

		Reference: We acknowledge the work of Yann H. Kerr and the VAS network team provided by the Climatology from Satellites Group (GCS) - University of Valencia in support of the ISMN;
		Variables: air temperature, soil moisture, soil temperature, 
		Soil Moisture Depths: 0.00 - 0.05 m
		Soil Moisture Sensors: Stevens Hydra Probe, ThetaProbe ML2X, 

	WATERLINE
		Abstract: 
		Continent: Europe
		Country: Greece
		Stations: 3
		Status: running
		Data Range: from 2021-07-10 
		Type: Project
		Url: https://www.waterlineproject.eu/
		Reference: We acknowledge the work of Prof Alexandra Gemitzi, Stavros Stathopoulos and the entire WATERLINE team and their contributions in support of the ISMN.
		Variables: air temperature, precipitation, soil moisture, 
		Soil Moisture Depths: 0.05 - 0.05 m
		Soil Moisture Sensors: Sentek Drill and drop, 

	WEGENERNET
		Abstract: The WegenerNet Feldbach Region is a unique weather and climate observation network comprising more than 150 hydrometeorological stations measuring temperature, humidity, precipitation, and at 14 locations also wind speed and direction. Soil moisture and soil temperature are measured at 12 stations, which are part of the International Soil Moisture Network (ISMN). 


The stations are located in a tightly spaced grid within a core area of 22 km x 16 km centered near the city of Feldbach in southeastern Austria.
With about one station every two square-km (area of about 300 square-km in total), and each station with 5-min time sampling, the network provides fully automated regular measurements since January 2007.


************************************************************************************************************
IMPORTANT NOTE: All data is on version 8.0 For further details please see https://wegenernet.org/downloads/Fuchsberger-etal_2023_WPSv8-release-notes.pdf

************************************************************************************************************

		Continent: Europe
		Country: Austria
		Stations: 13
		Status: running
		Data Range: from 2007-01-01 
		Type: project
		Url: http://www.wegenernet.org/;http://www.wegcenter.at/wegenernet
		Reference: Fuchsberger, J., Kirchengast, G. & Kabas, T. (2021), WegenerNet high-resolution weather and climate data from 2007 to 2020, Earth Syst. Sci. Data, 13, 1307–1334, https://doi.org/10.5194/essd-13-1307-2021, 2021;

Kirchengast, G., Kabas, T., Leuprecht, A., Bichler, C. & Truhetz, H. (2014), ‘Wegenernet: A pioneering high-resolution network for monitoring weather and climate’, Bulletin of the American Meteorological Society 95, https://doi.org/10.1175/BAMS-D-11-00161.1;
		Variables: air temperature, precipitation, soil moisture, soil temperature, 
		Soil Moisture Depths: 0.20 - 0.20 m, 0.30 - 0.30 m
		Soil Moisture Sensors: Hydraprobe II, pF-Meter, 

	WSMN
		Abstract: The WSMN network is located in Wales, Great Britain, and consists of six stations. The datasets are collected by the Aberystwyth University and are available since September 2011.
		Continent: Europe
		Country: UK
		Stations: 8
		Status: running
		Data Range: from 2013-07-11 
		Type: project
		Url: http://www.aber.ac.uk/wsmn
		Reference: Petropoulos, G. P. & McCalmont, J. P. (2017), ‘An operational in situ soil moisture & soil temperature monitoring network for west wales, uk: The wsmn network’, Sensors 17(7), 1481, https://doi.org/10.3390/s17071481;

		Variables: soil moisture, soil temperature, 
		Soil Moisture Depths: 0.02 - 0.02 m, 0.05 - 0.05 m, 0.10 - 0.10 m
		Soil Moisture Sensors: CS615, CS616, CS655, 

	XMS-CAT
		Abstract: The soil monitoring network is a set of stations with continuous data recording of physics parameters (temperature and moisture of soil) and environmental parameters such as pluviometry, temperature, relative air humidity and solar radiation. Project started at Tremp basin’s, in the crops of vineyards, and it has been continued in high altitude vineyard form Pre-pyrenees and Pyrenees. The main features that set up the stations are the sensors installed into the soils and the basic operation elements, such as the acquisition data system, the power system and the data transmission system. Generally, there are 4 multi parametric sensors to 5, 20, 50 and 100 cm of depth, when parent material allows it, these sensors measure soil moisture and temperature. Each station also has environmental sensors such as a rain gauge, a pyranometer and a air temperature and relative humidity probes for the necessary comparison of the soil and environmental parameters.
		Continent: Europe
		Country: Spain
		Stations: 18
		Status: running
		Data Range: from 2016-08-01 
		Type: project
		Url: https://visors.icgc.cat/mesurasols/#9/42.1765/1.1132
		Reference: We acknowledge the work of Agnès Lladós and Lola Boquera as well as the XMS-CAT network team in support of the ISMN.
		Variables: air temperature, precipitation, soil moisture, soil temperature, 
		Soil Moisture Depths: 0.05 - 0.05 m, 0.10 - 0.10 m, 0.20 - 0.20 m, 0.30 - 0.30 m, 0.40 - 0.40 m, 0.50 - 0.50 m, 0.60 - 0.60 m, 0.70 - 0.70 m, 0.75 - 0.75 m, 1.00 - 1.00 m
		Soil Moisture Sensors: CS655, DeltaOHM, SoilVUE10, 

