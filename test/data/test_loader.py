from settings import Settings
from data.loader import Loader
import pytest

result = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<style>
table, th, td {
  border:1px solid black;
}
</style>
<body>
<h2>You searched detail 'Pin 193'</h2>


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
                <td>Engine 2l</td>
                <td>Car</td>
                <td>8.0</td>
            </tr>
        
            <tr>
                <td></td>
                <td></td>
                <td>Wheel</td>
                <td>Bike</td>
                <td>4.0</td>
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
                <td>Stamp</td>
                <td>Car</td>
                <td>14.0</td>
            </tr>


</table>

</body>
</html>
"""


def format_text(text):
    return text.replace(' ', '').replace('\n', '')


@pytest.mark.asyncio
async def test_loader():
    settings = Settings(r'.\test\settings.json')
    assert settings.status

    loader = Loader(settings)
    detail = 'Pin 193'
    loaded = await loader.load([detail])
    assert format_text(loaded[detail]) == format_text(result)

