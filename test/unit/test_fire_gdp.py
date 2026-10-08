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


if __name__ == '__main__':
    unittest.main()
