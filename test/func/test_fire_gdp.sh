test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_plot_runs python src/plot_fire_gdp.py \
    --co2_file 'test/data/Agrofood_co2_emission_test.csv' \
    --gdp_file 'test/data/IMF_GDP_test.csv' \
    --out_file 'canada_gdp_emissions.png' \
    --title 'GDP vs Forest Fire Emissions in Canada' \
    --y_axis_label 'Forest Fire Emissions' \
    --y_variable 'Forest fires' \
    --country 'Canada'
assert_exit_code 0
assert_equal canada_gdp_emissions.png $( ls canada_gdp_emissions.png )
rm canada_gdp_emissions.png

run test_gdp_file_not_found python src/plot_fire_gdp.py \
    --co2_file 'test/data/Agrofood_co2_emission_test.csv' \
    --gdp_file 'test/data/IMF_GFP_test.csv' \
    --out_file 'canada_gdp_emissions.png' \
    --title 'GDP vs Forest Fire Emissions in Canada' \
    --y_axis_label 'Forest Fire Emissions' \
    --y_variable 'Forest fires' \
    --country 'Canada'

assert_exit_code 1
assert_in_stderr "Could not find test/data/IMF_GFP_test.csv"

run test_co2_file_not_found python src/plot_fire_gdp.py \
    --co2_file 'test/data/Agrofood_co2_emision_test.csv' \
    --gdp_file 'test/data/IMF_GFP_test.csv' \
    --out_file 'canada_gdp_emissions.png' \
    --title 'GDP vs Forest Fire Emissions in Canada' \
    --y_axis_label 'Forest Fire Emissions' \
    --y_variable 'Forest fires' \
    --country 'Canada'

assert_exit_code 1
assert_in_stderr "Could not find test/data/Agrofood_co2_emision_test.csv"

run test_missing_country python src/plot_fire_gdp.py \
    --co2_file 'test/data/Agrofood_co2_emission_test.csv' \
    --gdp_file 'test/data/IMF_GFP_test.csv' \
    --out_file 'gondor_gdp_emissions.png' \
    --title 'GDP vs Forest Fire Emissions in Gondor' \
    --y_axis_label 'Forest Fire Emissions' \
    --y_variable 'Forest fires' \
    --country 'Gondor'

assert_exit_code 1
assert_in_stderr "Gondor is not a country in test/data/Agrofood_co2_emission_test.csv and/or test/data/IMF_GFP_test.csv"