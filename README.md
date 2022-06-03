# WSCS4b_line
[![build](https://github.com/Yuluuuuan/WSCS4b_line/actions/workflows/build.yml/badge.svg)](https://github.com/Yuluuuuan/WSCS4b_line/actions/workflows/build.yml)
[![unit_test](https://github.com/Yuluuuuan/WSCS4b_line/actions/workflows/unit_test.yml/badge.svg)](https://github.com/Yuluuuuan/WSCS4b_line/actions/workflows/unit_test.yml)

This is a Brane package for data visualization. Draw line.

Make sure you have brane installed.

Import the package as follows:
```bash
$ brane import Yuluuuuan/WSCS4b_line
```
Set the environment variable. It shows where the data files are.

```bash
$ export CSV_PATH='/data'
$ export OUTPUT_PATH='/data'
```

There are four functions in this package:

`grouped(df, key, freq, col)` \
`add_time(df, key, freq, col)`\
`draw_line(csv_path:str,output_path:str)` \
`draw_pre(csv_path:str,output_path:str)`,\
for .we can get 

You can `test` the package to get an overview of these functions and corresponding parameters:
```bash
$ brane --debug test line
```

You should push the package into your brane instance to be able to import it in your remote session or jupyterlab notebook.
```bash
$ brane push line
```
