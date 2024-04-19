import unittest
import mean_var_std
import demographic_data_analyzer
import unittest
import medical_data_visualizer
import matplotlib as mpl

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = mean_var_std.calculate([2,6,2,8,4,0,1,5,7])
        expected = {'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889], 'variance': [[9.555555555555557, 0.6666666666666666, 8.666666666666666], [3.555555555555556, 10.666666666666666, 6.222222222222221], 6.987654320987654], 'standard deviation': [[3.091206165165235, 0.816496580927726, 2.943920288775949], [1.8856180831641267, 3.265986323710904, 2.494438257849294], 2.6434171674156266], 'max': [[8, 6, 7], [6, 8, 7], 8], 'min': [[1, 4, 0], [2, 0, 1], 0], 'sum': [[11, 15, 9], [10, 12, 13], 35]}
        self.assertAlmostEqual(actual, expected, "Expected different output when calling 'calculate()' with '[2,6,2,8,4,0,1,5,7]'")

    def test_calculate2(self):
        actual = mean_var_std.calculate([9,1,5,3,3,3,2,9,0])
        expected = {'mean': [[4.666666666666667, 4.333333333333333, 2.6666666666666665], [5.0, 3.0, 3.6666666666666665], 3.888888888888889], 'variance': [[9.555555555555555, 11.555555555555557, 4.222222222222222], [10.666666666666666, 0.0, 14.888888888888891], 9.209876543209875], 'standard deviation': [[3.0912061651652345, 3.39934634239519, 2.0548046676563256], [3.265986323710904, 0.0, 3.8586123009300755], 3.0347778408328137], 'max': [[9, 9, 5], [9, 3, 9], 9], 'min': [[2, 1, 0], [1, 3, 0], 0], 'sum': [[14, 13, 8], [15, 9, 11], 35]}
        self.assertAlmostEqual(actual, expected, "Expected different output when calling 'calculate()' with '[9,1,5,3,3,3,2,9,0]'")
    
    def test_calculate_with_few_digits(self):
        self.assertRaisesRegex(ValueError, "List must contain nine numbers.", mean_var_std.calculate, [2,6,2,8,4,0,1,])

if __name__ == "__main__":
    unittest.main()

class DemographicAnalyzerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.data = demographic_data_analyzer.calculate_demographic_data(print_data = False)

    def test_race_count(self):
        actual = self.data['race_count'].tolist()
        expected = [27816, 3124, 1039, 311, 271]
        self.assertCountEqual(actual, expected, msg="Expected race count values to be [27816, 3124, 1039, 311, 271]")

    def test_average_age_men(self):
        actual = self.data['average_age_men']
        expected = 39.4
        self.assertAlmostEqual(actual, expected, msg="Expected different value for average age of men.")

    def test_percentage_bachelors(self):
        actual = self.data['percentage_bachelors']
        expected = 16.4 
        self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage with Bachelors degrees.")

    def test_higher_education_rich(self):
        actual = self.data['higher_education_rich']
        expected = 46.5
        self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage with higher education that earn >50K.")
  
    def test_lower_education_rich(self):
        actual = self.data['lower_education_rich']
        expected = 17.4
        self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage without higher education that earn >50K.")

    def test_min_work_hours(self):
        actual = self.data['min_work_hours']
        expected = 1
        self.assertAlmostEqual(actual, expected, msg="Expected different value for minimum work hours.")     

    def test_rich_percentage(self):
        actual = self.data['rich_percentage']
        expected = 10
        self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage of rich among those who work fewest hours.")   

    def test_highest_earning_country(self):
        actual = self.data['highest_earning_country']
        expected = 'Iran'
        self.assertEqual(actual, expected, "Expected different value for highest earning country.")   

    def test_highest_earning_country_percentage(self):
        actual = self.data['highest_earning_country_percentage']
        expected = 41.9
        self.assertAlmostEqual(actual, expected, msg="Expected different value for highest earning country percentage.")   

    def test_top_IN_occupation(self):
        actual = self.data['top_IN_occupation']
        expected = 'Prof-specialty'
        self.assertEqual(actual, expected, "Expected different value for top occupations in India.")      

if __name__ == "__main__":
    unittest.main()

class CatPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.draw_cat_plot()
        self.ax = self.fig.axes[0]
    
    def test_line_plot_labels(self):
        actual = self.ax.get_xlabel()
        expected = "variable"
        self.assertEqual(actual, expected, "Expected line plot xlabel to be 'variable'")
        actual = self.ax.get_ylabel()
        expected = "total"
        self.assertEqual(actual, expected, "Expected line plot ylabel to be 'total'")
        actual = []
        for label in self.ax.get_xaxis().get_majorticklabels():
            actual.append(label.get_text())
        expected = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
        self.assertEqual(actual, expected, "Expected bar plot secondary x labels to be 'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'")

    def test_bar_plot_number_of_bars(self):
        actual = len([rect for rect in self.ax.get_children() if isinstance(rect, mpl.patches.Rectangle)])
        expected = 13
        self.assertEqual(actual, expected, "Expected a different number of bars chart.")


class HeatMapTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.draw_heat_map()
        self.ax = self.fig.axes[0]

    def test_heat_map_labels(self):
        actual = []
        for label in self.ax.get_xticklabels():
          actual.append(label.get_text())
        expected = ['id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']
        self.assertEqual(actual, expected, "Expected heat map labels to be 'id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight'.")
    
    def test_heat_map_values(self):
        actual = [text.get_text() for text in self.ax.get_default_bbox_extra_artists() if isinstance(text, mpl.text.Text)]
        print(actual)
        expected = ['0.0', '0.0', '-0.0', '0.0', '-0.1', '0.5', '0.0', '0.1', '0.1', '0.3', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.2', '0.1', '0.0', '0.2', '0.1', '0.0', '0.1', '-0.0', '-0.1', '0.1', '0.0', '0.2', '0.0', '0.1', '-0.0', '-0.0', '0.1', '0.0', '0.1', '0.4', '-0.0', '-0.0', '0.3', '0.2', '0.1', '-0.0', '0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.2', '0.1', '0.1', '0.0', '0.0', '0.0', '0.0', '0.3', '0.0', '-0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.0', '0.0', '-0.0', '0.0', '0.0', '0.0', '0.2', '0.0', '-0.0', '0.2', '0.1', '0.3', '0.2', '0.1', '-0.0', '-0.0', '-0.0', '-0.0', '0.1', '-0.1', '-0.1', '0.7', '0.0', '0.2', '0.1', '0.1', '-0.0', '0.0', '-0.0', '0.1']
        self.assertEqual(actual, expected, "Expected different values in heat map.")

if __name__ == "__main__":
    unittest.main()
