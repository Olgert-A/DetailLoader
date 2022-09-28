from settings import Settings
from data.parser import Parser

html_text = """
<!DOCTYPE html>
<html>
<style>
table, th, td {
  border:1px solid black;
}
</style>
<body>

<table style="width:100%">
  <tr>
    <th>Detail</th>
    <th>Status</th>
    <th>Part_of</th>
    <th>Product</th>
    <th>Amount</th>
  </tr>
  <tr>
    <td>Pin 193</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>Active</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>Engine</td>
    <td>Auto</td>
    <td>8</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>Wheel</td>
    <td>Moto</td>
    <td>4</td>
  </tr>
  <tr>
    <td></td>
    <td>Archive</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>Form</td>
    <td>Stamp</td>
    <td>14</td>
  </tr>
  <tr>
    <td>Pin 205</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>Active</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>Hull</td>
    <td>Boat</td>
    <td>256</td>
  </tr>
</table>
</body>
</html>
"""


def test_parser():
    settings = Settings(r'.\test\settings.json')
    assert settings.status

    parser = Parser(settings)
    data = parser.parse({'Pin 193': html_text})
    result = {'Pin 193': [('Engine', 'Auto', 8.0), ('Wheel', 'Moto', 4.0)]}
    assert data == result
