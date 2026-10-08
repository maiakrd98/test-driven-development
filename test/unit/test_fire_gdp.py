import os
import sys
import unittest
sys.path.append("src")  # noqa
import fire_gdp


class TestGetColumnIndex(unittest.TestCase):

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
        header, result = fire_gdp.get_data("test/data/"
                                           "Agrofood_co2_emission_test.csv",
                                           return_header=True)
        self.assertEqual(result, expected_result)
        self.assertEqual(header, expected_header)

    def test_one_country(self):
        expected_result = [["Spain", "2016", "23.2659", "1400.3544"],
                           ["Spain", "2017", "62.4373", "1001.3977"],
                           ["Spain", "2018", "3.511", "1450.7849"],
                           ["Spain", "2019", "17.5455", "1190.6392"],
                           ["Spain", "2020", "6.1089", "1548.3999"]]
        result = fire_gdp.get_data("test/data/"
                                   "Agrofood_co2_emission_test.csv",
                                   query_column=0,
                                   query_value="Spain")
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
