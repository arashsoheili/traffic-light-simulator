from app.trafficlight import TrafficLight

green = "\n      ##\n     _[]_\n    [____]\n.----'  '----.\n|    .==.    |\n|   /\x1b[31m    \x1b[0m\\   |\n|   \\\x1b[31m    \x1b[0m/   |\n|    .==.    |\n|    .==.    |\n|   /\x1b[33m    \x1b[0m\\   |\n|   \\\x1b[33m    \x1b[0m/   |\n|    .==.    |\n|    .==.    |\n|   /\x1b[32m####\x1b[0m\\   |\n|   \\\x1b[32m####\x1b[0m/   |\n|    .==.    |\n'--.______.--'\n\n"

yellow = "\n      ##\n     _[]_\n    [____]\n.----'  '----.\n|    .==.    |\n|   /\x1b[31m    \x1b[0m\\   |\n|   \\\x1b[31m    \x1b[0m/   |\n|    .==.    |\n|    .==.    |\n|   /\x1b[33m####\x1b[0m\\   |\n|   \\\x1b[33m####\x1b[0m/   |\n|    .==.    |\n|    .==.    |\n|   /\x1b[32m    \x1b[0m\\   |\n|   \\\x1b[32m    \x1b[0m/   |\n|    .==.    |\n'--.______.--'\n\n"

red = "\n      ##\n     _[]_\n    [____]\n.----'  '----.\n|    .==.    |\n|   /\x1b[31m####\x1b[0m\\   |\n|   \\\x1b[31m####\x1b[0m/   |\n|    .==.    |\n|    .==.    |\n|   /\x1b[33m    \x1b[0m\\   |\n|   \\\x1b[33m    \x1b[0m/   |\n|    .==.    |\n|    .==.    |\n|   /\x1b[32m    \x1b[0m\\   |\n|   \\\x1b[32m    \x1b[0m/   |\n|    .==.    |\n'--.______.--'\n\n"


def test_green_light(capsys):
    light = TrafficLight()
    light.show()
    captured = capsys.readouterr()
    assert captured.out == green


def test_yellow_light(capsys):
    light = TrafficLight()
    light.change_light()
    light.show()
    captured = capsys.readouterr()
    assert captured.out == yellow


def test_red_light(capsys):
    light = TrafficLight()
    light.change_light()
    light.change_light()
    light.show()
    captured = capsys.readouterr()
    assert captured.out == red
