# Data Dictionary

## Project

**Project title:** Using Machine Learning to Identify High-Risk Police
Stations for Serious Violent Crime in South Africa

**Stakeholder:** South African Police Service (SAPS)

**Unit of analysis:** Police station × financial year

**Prediction task:** Use information available for a police station in
the current financial year to classify its serious violent crime risk in
the following financial year as **Lower Risk (0)** or **Higher Risk
(1)**.

**Raw dataset:** South African Police Service Annual Crime Records
2005-2026, Version 1.4.

**Dataset source / citation:**\
South African Police Service. *South African Police Service Annual Crime
Records 2005-2026* \[dataset\]. Version 1.4. Pretoria: South African
Police Service (SAPS) \[producers\], 2026. Pretoria: DataFirst
\[distributor\], 2026.\
DOI: https://doi.org/10.25828/5MAW-4H90

------------------------------------------------------------------------

## 1. Raw Dataset Fields

The source CSV contains **24,206 rows and 38 columns**.

### Identification and geographic fields

  ------------------------------------------------------------------------
  Field             Type              Role              Description
  ----------------- ----------------- ----------------- ------------------
  `year`            object/string     Time              Financial year
                                                        associated with
                                                        the police-station
                                                        crime record.

  `station`         object/string     Identifier        Police station
                                                        name/identifier.
                                                        Used to identify
                                                        the station and to
                                                        construct the
                                                        station-level
                                                        chronological
                                                        target.

  `loc_mn`          object/string     Categorical       Local municipality
                                      feature           associated with
                                                        the police
                                                        station.

  `dc_mn`           object/string     Categorical       District
                                      feature           municipality
                                                        associated with
                                                        the police
                                                        station.

  `longitude`       float             Numerical feature Longitude
                                                        coordinate
                                                        associated with
                                                        the police
                                                        station.

  `latitude`        float             Numerical feature Latitude
                                                        coordinate
                                                        associated with
                                                        the police
                                                        station.
  ------------------------------------------------------------------------

### Crime-count fields

The following variables are crime counts recorded for a police station
and financial year. They are used as predictive features unless
otherwise stated.

  ----------------------------------------------------------------------------------
  Field                      Type              Role              Description
  -------------------------- ----------------- ----------------- -------------------
  `other_theft`              integer           Feature           Recorded count for
                                                                 other theft.

  `arson`                    integer           Feature           Recorded count for
                                                                 arson.

  `assault_gbh`              integer           Feature / target  Recorded count for
                                               component         assault with intent
                                                                 to inflict grievous
                                                                 bodily harm.

  `attempted_murder`         integer           Feature / target  Recorded count for
                                               component         attempted murder.

  `attempted_sexoff`         integer           Feature           Recorded count for
                                                                 attempted sexual
                                                                 offences.

  `bank_robbery`             integer           Feature           Recorded count for
                                                                 bank robbery.

  `burglary_nonres`          integer           Feature           Recorded count for
                                                                 burglary at
                                                                 non-residential
                                                                 premises.

  `burglary_res`             integer           Feature           Recorded count for
                                                                 burglary at
                                                                 residential
                                                                 premises.

  `carjacking`               integer           Feature           Recorded count for
                                                                 carjacking.

  `commercial_crime`         integer           Feature           Recorded count for
                                                                 commercial crime.

  `common_assault`           integer           Feature           Recorded count for
                                                                 common assault.

  `common_robbery`           integer           Feature           Recorded count for
                                                                 common robbery.

  `contact_sexoff`           integer           Feature           Recorded count for
                                                                 contact-related
                                                                 sexual offences.

  `dui`                      integer           Feature           Recorded count for
                                                                 driving under the
                                                                 influence-related
                                                                 offences.

  `drug_crime`               integer           Feature           Recorded count for
                                                                 drug-related crime.

  `illegal_firearms`         integer           Feature           Recorded count for
                                                                 illegal
                                                                 firearms-related
                                                                 offences.

  `kidnapping`               integer           Feature / target  Recorded count for
                                               component         kidnapping.

  `malicious_damage`         integer           Feature           Recorded count for
                                                                 malicious damage to
                                                                 property.

  `murder`                   integer           Feature / target  Recorded count for
                                               component         murder.

  `rape`                     integer           Feature / target  Recorded count for
                                               component         rape.

  `robbery_nonres`           integer           Feature           Recorded count for
                                                                 robbery at
                                                                 non-residential
                                                                 premises.

  `robbery_res`              integer           Feature           Recorded count for
                                                                 robbery at
                                                                 residential
                                                                 premises.

  `cash_transit_robbery`     integer           Feature           Recorded count for
                                                                 cash-in-transit
                                                                 robbery.

  `aggr_robbery`             integer           Feature           Recorded count for
                                                                 aggravated robbery.

  `sexual_assault`           integer           Feature / target  Recorded count for
                                               component         sexual assault.

  `sexual_offences`          float             Feature           Recorded count for
                                                                 sexual offences.
                                                                 Retained as a
                                                                 predictive feature;
                                                                 it was not included
                                                                 directly in the
                                                                 serious violent
                                                                 crime target
                                                                 because of
                                                                 missingness and
                                                                 overlap
                                                                 considerations.

  `police_detected_sexoff`   integer           Feature           Recorded count for
                                                                 police-detected
                                                                 sexual offences.

  `shoplifting`              integer           Feature           Recorded count for
                                                                 shoplifting.

  `stock_theft`              integer           Feature           Recorded count for
                                                                 stock theft.

  `vehicle_theft`            integer           Feature           Recorded count for
                                                                 vehicle theft.

  `theft_from_vehicle`       integer           Feature           Recorded count for
                                                                 theft from a motor
                                                                 vehicle.

  `truck_hijacking`          integer           Feature           Recorded count for
                                                                 truck hijacking.
  ----------------------------------------------------------------------------------

------------------------------------------------------------------------

## 2. Derived Project Variables

The following variables are created during the project and are **not
original columns in the raw CSV**.

  -------------------------------------------------------------------------------------
  Variable                  Type              Role              Description
  ------------------------- ----------------- ----------------- -----------------------
  `start_year`              integer           Feature / time    Starting year extracted
                                              index             from the financial-year
                                                                field and used to
                                                                create the
                                                                chronological
                                                                train/validation/test
                                                                split.

  `serious_violent_crime`   numerical         Intermediate      Current-year serious
                                              target component  violent crime score
                                                                constructed from
                                                                murder, attempted
                                                                murder, rape, sexual
                                                                assault, assault GBH
                                                                and kidnapping.

  `next_year_score`         numerical         Intermediate      Serious violent crime
                                              target component  score for the following
                                                                financial year for the
                                                                same police station.

  `next_year_start`         integer           Target alignment  Starting year of the
                                                                following
                                                                financial-year
                                                                observation used for
                                                                target construction.

  `consecutive_year`        boolean           Target-quality    Indicates whether the
                                              flag              current and next
                                                                observations represent
                                                                consecutive financial
                                                                years for the same
                                                                station.

  `risk_class`              binary integer    Final target      Classification target:
                                                                `0 = Lower Risk`,
                                                                `1 = Higher Risk`.
  -------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 3. Serious Violent Crime Target

The serious violent crime score is constructed from six components:

1.  `murder`
2.  `attempted_murder`
3.  `rape`
4.  `sexual_assault`
5.  `assault_gbh`
6.  `kidnapping`

Negative values in these target components are treated as invalid and
converted to missing values before target construction.

The target is shifted one financial year forward within each police
station so that current-year information is used to predict the
following year's risk.

Only consecutive station-year observations are used for the
one-year-ahead target.

The higher-risk threshold is based on the **75th percentile of the
training data**, which was **326.0** in this project.

Therefore:

-   `risk_class = 0` → Lower Risk
-   `risk_class = 1` → Higher Risk

------------------------------------------------------------------------

## 4. Model Input Features

The final modelling feature set contains **37 input features**:

### Crime features

All 32 crime variables in the raw dataset are used as predictive
features, including `sexual_offences`.

### Geographic/time features

-   `loc_mn`
-   `dc_mn`
-   `longitude`
-   `latitude`
-   `start_year`

The following fields are **not used as model inputs**:

-   `station`
-   `risk_class`
-   `next_year_score`
-   `next_year_start`
-   `consecutive_year`
-   `serious_violent_crime`

The station identifier is excluded from the predictors to avoid allowing
the model to simply memorise station identity.

------------------------------------------------------------------------

## 5. Preprocessing

The final preprocessing pipeline performs the following operations:

### Numerical variables

1.  Invalid negative crime counts are converted to missing values.
2.  Missing numerical values are imputed using the median calculated
    from training data.
3.  Numerical variables are standardised using `StandardScaler`.

### Categorical variables

1.  Missing categorical values are imputed using the most frequent
    category.
2.  `loc_mn` and `dc_mn` are one-hot encoded.
3.  Unknown categories encountered during prediction are handled using
    `handle_unknown="ignore"`.

The preprocessing is part of the saved machine-learning pipeline so that
the same transformations are applied during deployment.

------------------------------------------------------------------------

## 6. Data Splitting

The project uses a chronological split because the model predicts a
future financial year:

  -----------------------------------------------------------------------
  Dataset                 Feature years           Purpose
  ----------------------- ----------------------- -----------------------
  Training                2005--2021              Model fitting and
                                                  learning preprocessing
                                                  parameters

  Validation              2022--2023              Model comparison, model
                                                  selection and
                                                  optimisation

  Test                    2024                    Final locked evaluation
                                                  only
  -----------------------------------------------------------------------

The test set is not used for model selection or hyperparameter tuning.

------------------------------------------------------------------------

## 7. Missing and Invalid Values

Important data-quality issues identified during the project include
missing geographic values and missing `sexual_offences` values.

Negative crime counts are treated as invalid rather than genuine
negative counts. The preprocessing pipeline converts negative crime
values to `NaN` and subsequently imputes them using training-set
medians.

The deployment interface additionally validates user input and rejects
negative crime counts before a prediction is made.

------------------------------------------------------------------------

## 8. Data Dictionary and Reproducibility Notes

This file documents both the raw dataset fields and the variables
created during modelling so that another user can understand:

-   what each input represents;
-   which variables are used as predictors;
-   how the target is constructed;
-   which variables are excluded;
-   how the chronological split is defined; and
-   how preprocessing is applied.

The project should be reproduced using the notebook, `requirements.txt`,
saved pipeline and Streamlit application supplied in this repository.
