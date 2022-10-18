# ncstudio_height_map
Тут три скрипта на python3, при помощи которых можно облегчить себе жизнь.
Как этим пользоваться:

1.В G-Code Ripper надо вставить свой gcode, он выдаст gcode для построения карты высот, но с кодом G31. К сожалению, ncstudio не знает такой команды, поэтому ее нужно заменить на G65 с макросом P1005(спасибо G-Host с форума mir-cnc.ru)

2.Заменяем при помощи 
> python g31_to_g65_p1005.py your_gcode.nc

3.Запускаем отредактированный your_gcode.nc на ЧПУ
4.Парсим лог NCSTUDIO.LOG при помощи
> python log_to_coords.py path_to_program_dir/NCSTUDIO.LOG

5.В каталоге с log_to_coords.py будет создан файл clean_coords.txt, но в машинных координатах, а не логических. 
6.Если нужные логические
> python recalc_to_zero_coord.py clean_coords.txt

7.Готово!
