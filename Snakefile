countries = ["Brazil", "Canada", "China", "Gabon", "Honduras", "India", "Afghanistan", "Algeria", "Angola", "Argentina", "Australia", "Bangladesh", "Botswana", "Egypt", "Sweden", "Spain", "Japan", "Kenya", "Malawi", "Mexico", "Peru", "Thailand", "Zambia"]

rule all:
    input:
        expand("plots/{country}_GDP_emissions.png", country=countries)

rule create_plots:
    input:
        co2="data/Agrofood_co2_emission.csv",
        gdp="data/IMF_GDP.csv"
    output:
        "plots/{country}_GDP_emissions.png"
    shell:
        """
        python src/plot_fire_gdp.py \
        --co2_file {input.co2} \
        --gdp_file {input.gdp} \
        --out_file {output} \
        --title 'GDP vs Carbon Emissions in {wildcards.country}' \
        --y_axis_label 'Total Emissions' \
        --y_variable 'total_emission' \
        --country {wildcards.country}
        """
