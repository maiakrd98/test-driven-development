import os
import sys
import unittest
import warnings
sys.path.append("src")  # noqa
import fire_gdp


class TestGetData(unittest.TestCase):

    def test_all_rows(self):
        expected_result = [["Canada", "2016", "812.7646", "3876.2419"],
                           ["Canada", "2017", "1248.7836", "3838.6631"],
                           ["Canada", "2018", "3236.4746", "3943.5181"],
                           ["Canada", "2019", "1336.7596", ""],
                           ["Canada", "2020", "222.2592", "4246.3211"],
                           ["Japan", "2016", "4.9336", "688.7746"],
                           ["Japan", "2017", "12.2035", "691.5795"],
                           ["Japan", "2018", "21.8108", "664.0262"],
                           ["Japan", "2019", "19.9939", "680.9674"],
                           ["Japan", "2020", "19.6038", "641.2642"],
                           ["Spain", "2016", "23.2659", "1400.3544"],
                           ["Spain", "2017", "62.4373", "1001.3977"],
                           ["Spain", "2018", "3.511", "1450.7849"],
                           ["Spain", "2019", "17.5455", "1190.6392"],
                           ["Spain", "2020", "6.1089", "1548.3999"],
                           ["United Republic of Tanzania",
                            "2016", "9208.313", "690.2927"],
                           ["United Republic of Tanzania",
                            "2017", "9517.3012", "731.7093"],
                           ["United Republic of Tanzania",
                            "2018", "7079.7641", "712.0791"],
                           ["United Republic of Tanzania",
                            "2019", "6978.071", "700.7068"],
                           ["United Republic of Tanzania",
                            "2020", "5876.0538", "859.0343"]]
        result = fire_gdp.get_data("test/data/Agrofood_co2_emission_test.csv")
        self.assertEqual(result, expected_result)

    def test_all_rows_return_header(self):
        expected_result = [["Canada", "2016", "812.7646", "3876.2419"],
                           ["Canada", "2017", "1248.7836", "3838.6631"],
                           ["Canada", "2018", "3236.4746", "3943.5181"],
                           ["Canada", "2019", "1336.7596", ""],
                           ["Canada", "2020", "222.2592", "4246.3211"],
                           ["Japan", "2016", "4.9336", "688.7746"],
                           ["Japan", "2017", "12.2035", "691.5795"],
                           ["Japan", "2018", "21.8108", "664.0262"],
                           ["Japan", "2019", "19.9939", "680.9674"],
                           ["Japan", "2020", "19.6038", "641.2642"],
                           ["Spain", "2016", "23.2659", "1400.3544"],
                           ["Spain", "2017", "62.4373", "1001.3977"],
                           ["Spain", "2018", "3.511", "1450.7849"],
                           ["Spain", "2019", "17.5455", "1190.6392"],
                           ["Spain", "2020", "6.1089", "1548.3999"],
                           ["United Republic of Tanzania",
                            "2016", "9208.313", "690.2927"],
                           ["United Republic of Tanzania",
                            "2017", "9517.3012", "731.7093"],
                           ["United Republic of Tanzania",
                            "2018", "7079.7641", "712.0791"],
                           ["United Republic of Tanzania",
                            "2019", "6978.071", "700.7068"],
                           ["United Republic of Tanzania",
                            "2020", "5876.0538", "859.0343"]]
        expected_header = ["Area", "Year", "Forest fires", "Crop Residues"]
        file_name = "test/data/Agrofood_co2_emission_test.csv"
        header, result = fire_gdp.get_data(file_name, return_header=True)
        self.assertEqual(result, expected_result)
        self.assertEqual(header, expected_header)

    def test_one_country(self):
        expected_result = [["Spain", "2016", "23.2659", "1400.3544"],
                           ["Spain", "2017", "62.4373", "1001.3977"],
                           ["Spain", "2018", "3.511", "1450.7849"],
                           ["Spain", "2019", "17.5455", "1190.6392"],
                           ["Spain", "2020", "6.1089", "1548.3999"]]
        file_name = "test/data/Agrofood_co2_emission_test.csv"
        result = fire_gdp.get_data(file_name,
                                   query_column=0,
                                   query_value="Spain")
        self.assertEqual(result, expected_result)

    def test_one_country_return_header(self):
        expected_result = [["Spain", "2016", "23.2659", "1400.3544"],
                           ["Spain", "2017", "62.4373", "1001.3977"],
                           ["Spain", "2018", "3.511", "1450.7849"],
                           ["Spain", "2019", "17.5455", "1190.6392"],
                           ["Spain", "2020", "6.1089", "1548.3999"]]
        expected_header = ["Area", "Year", "Forest fires", "Crop Residues"]
        file_name = "test/data/Agrofood_co2_emission_test.csv"
        header, result = fire_gdp.get_data(file_name,
                                           query_column=0,
                                           query_value="Spain",
                                           return_header=True)
        self.assertEqual(result, expected_result)
        self.assertEqual(header, expected_header)

    def test_query_col_no_query_val(self):
        file_name = "test/data/Agrofood_co2_emission_test.csv"
        with self.assertRaises(SystemExit) as cm:
            fire_gdp.get_data(file_name, query_column=0)
        self.assertEqual("You input a query_column, but not a query_value, "
                         "please enter either both or neither",
                         str(cm.exception))

    def test_query_val_no_query_col(self):
        file_name = "test/data/Agrofood_co2_emission_test.csv"
        with self.assertRaises(SystemExit) as cm:
            fire_gdp.get_data(file_name, query_value="Japan")
        self.assertEqual("You input a query_value, but not a query_column, "
                         "please enter either both or neither",
                         str(cm.exception))

    def test_query_val_not_present(self):
        file_name = "test/data/Agrofood_co2_emission_test.csv"

        with self.assertWarns(UserWarning) as cm:
            result = fire_gdp.get_data(file_name, query_column=0,
                                       query_value="Gondor")

        self.assertEqual("The query_value you entered ('Gondor') "
                         "is not present",
                         str(cm.warning))
        self.assertIsNone(result)

    def test_file_not_found(self):
        file_name = "test/data/Agrofood_co2_emision_test.csv"
        with self.assertRaises(SystemExit) as cm:
            fire_gdp.get_data(file_name)
        self.assertEqual("Could not find test/data/"
                         "Agrofood_co2_emision_test.csv",
                         str(cm.exception))

    def test_index_out_of_bounds(self):
        file_name = "test/data/Agrofood_co2_emission_test.csv"
        with self.assertRaises(SystemExit) as cm:
            fire_gdp.get_data(file_name, query_column=44, query_value="Canada")
        self.assertEqual("query_column index (44) is out of bounds",
                         str(cm.exception))


class TestGetColumnIndex(unittest.TestCase):

    def test_name_present(self):
        header = ["Area", "Year", "Forest fires", "Crop Residues"]
        col_index = fire_gdp.get_column_index(header, "Forest fires")
        self.assertEqual(col_index, 2)

    def test_name_ansent(self):
        header = ["Area", "Year", "Forest fires", "Crop Residues"]
        col_index = fire_gdp.get_column_index(header, "Cows")
        self.assertIsNone(col_index)

    def test_empty_header(self):
        header = []
        with self.assertWarns(UserWarning) as cm:
            col_index = fire_gdp.get_column_index(header, "Cows")

        self.assertEqual("Warning: you have entered an empty header",
                         str(cm.warning))
        self.assertIsNone(col_index)

    def test_none_header(self):
        with self.assertWarns(UserWarning) as cm:
            col_index = fire_gdp.get_column_index(None, "Cows")

        self.assertEqual("Warning: you have entered None as a header",
                         str(cm.warning))
        self.assertIsNone(col_index)


class TestGetFireGdpYearData(unittest.TestCase):

    def test_canada_fires(self):
        co2_file = "test/data/Agrofood_co2_emission_test.csv"
        gdp_file = "test/data/IMF_GDP_test.csv"
        result = fire_gdp.get_fire_gdp_year_data(co2_file, gdp_file, "Canada")

        expected_result = [[2016, 812.7646, 2025535.00],
                           [2017, 1248.7836, 2140641.00],
                           [2018, 3236.4746, 2235675.00],
                           [2019, 1336.7596, 2313563.00],
                           [2020, 222.2592, 2209681.00]]

        self.assertEqual(result, expected_result)

    def test_japan_fires(self):
        co2_file = "test/data/Agrofood_co2_emission_test.csv"
        gdp_file = "test/data/IMF_GDP_test.csv"

        with self.assertWarns(UserWarning) as cm:
            result = fire_gdp.get_fire_gdp_year_data(co2_file,
                                                     gdp_file,
                                                     "Japan")

        self.assertEqual("The country you entered ('Japan') "
                         "is not present in the gdp_file "
                         "('test/data/IMF_GDP_test.csv')",
                         str(cm.warning))
        self.assertIsNone(result)

    def test_sweden_fires(self):
        co2_file = "test/data/Agrofood_co2_emission_test.csv"
        gdp_file = "test/data/IMF_GDP_test.csv"

        with self.assertWarns(UserWarning) as cm:
            result = fire_gdp.get_fire_gdp_year_data(co2_file,
                                                     gdp_file,
                                                     "Sweden")

        self.assertEqual("The country you entered ('Sweden') "
                         "is not present in the co2_file "
                         "('test/data/Agrofood_co2_emission_test.csv')",
                         str(cm.warning))
        self.assertIsNone(result)

    def test_spain_crops(self):
        co2_file = "test/data/Agrofood_co2_emission_test.csv"
        gdp_file = "test/data/IMF_GDP_test.csv"
        em_name = "Crop Residues"

        result = fire_gdp.get_fire_gdp_year_data(co2_file,
                                                 gdp_file,
                                                 "Spain",
                                                 emission_col_name=em_name)

        expected_result = [[2016, 1400.3544, 1114420.00],
                           [2017, 1001.3977, 1162492.00],
                           [2018, 1450.7849, 1203859.00],
                           [2019, 1190.6392, 1245513.00],
                           [2020, 1548.3999, 1119010.00]]

        self.assertEqual(result, expected_result)

    def test_canada_crops(self):
        co2_file = "test/data/Agrofood_co2_emission_test.csv"
        gdp_file = "test/data/IMF_GDP_test.csv"
        em_name = "Crop Residues"

        result = fire_gdp.get_fire_gdp_year_data(co2_file,
                                                 gdp_file,
                                                 "Canada",
                                                 emission_col_name=em_name)

        expected_result = [[2016, 3876.2419, 2025535.00],
                           [2017, 3838.6631, 2140641.00],
                           [2018, 3943.5181, 2235675.00],
                           [2020, 4246.3211, 2209681.00]]

        self.assertEqual(result, expected_result)

    def test_tanzania_crops(self):
        co2_file = "test/data/Agrofood_co2_emission_test.csv"
        gdp_file = "test/data/IMF_GDP_test.csv"
        em_name = "Crop Residues"
        country = "United Republic of Tanzania"

        result = fire_gdp.get_fire_gdp_year_data(co2_file,
                                                 gdp_file,
                                                 country,
                                                 emission_col_name=em_name)

        expected_result = [[2018, 712.0791, 123989405.68],
                           [2019, 700.7068, 134383845.93],
                           [2020, 859.0343, 145429645.07]]

        self.assertEqual(result, expected_result)

    def test_nonexistent_emission_name(self):
        co2_file = "test/data/Agrofood_co2_emission_test.csv"
        gdp_file = "test/data/IMF_GDP_test.csv"
        country = "United Republic of Tanzania"

        with self.assertWarns(UserWarning) as cm:
            result = fire_gdp.get_fire_gdp_year_data(co2_file,
                                                     gdp_file,
                                                     country,
                                                     emission_col_name="Cows")

        self.assertEqual("There is no column in 'test/data/Agrofood_co2"
                         "_emission_test.csv' titled 'Cows'",
                         str(cm.warning))
        self.assertIsNone(result)

    def test_conversion_error(self):
        co2_file = "test/data/Agrofood_co2_emission_test.csv"
        gdp_file = "test/data/IMF_GDP_test.csv"

        with self.assertRaises(SystemExit) as cm:
            fire_gdp.get_fire_gdp_year_data(co2_file,
                                            gdp_file,
                                            "Canada",
                                            emission_col_name="Area")

        self.assertEqual("Unable to convert 'Canada' to float",
                         str(cm.exception))


if __name__ == '__main__':
    unittest.main()
