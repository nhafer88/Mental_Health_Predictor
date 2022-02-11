create table us_cities (
    city varchar not null,
    state_id varchar not null,
    state_name varchar not null,
    county_fips varchar not null,
    county_name varchar not null,
    population int not null,
    density int not null,
    military bool not null,
    incorporated bool not null,
    zips varchar not null,
);

create table income (
    id int not null,
    State_Name varchar not null,
    State_ab varchar not null,
    County varchar not null,
    City varchar not null,
    Zip_Code varchar not null,
    Area_Code varchar not null,
    ALand int not null,
    AWater int not null,
    Mean decimal not null,
    Median int not null,
    Stdev varchar not null
);

create table mental_health(
    Year varchar not null,
    StateAbbr varchar not null,
    StateDesc varchar not null,
    CityName varchar not null,
    GeographicLevel varchar not null,
    Data_Value float not null,
    High_Confidence_Limit float not null,
    PopulationCount int not null,
    CityFIPS float not null
);

