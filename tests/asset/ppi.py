banner_lex_cn = {
    'month': '月份',
    'ppiip': '工业品出厂',
    'ppi': '生产资料',
    'qm': '采掘工业',
    'rmi': '原材料',
    'pi': '加工工业',
    'cg': '生活资料',
    'food': '食品',
    'clothing': '衣着',
    'roeu': '一般日用品',
    'dcg': '耐用消费品',
}

banner_lex = {
    'month': 'Month',
    'ppiip': 'Industrial',
    'ppi': 'Capital',
    'qm': 'Mining',
    'rmi': 'Raw material',
    'pi': 'Processing ind',
    'cg': 'Consumer goods',
    'food': 'Food',
    'clothing': 'Clothing',
    'roeu': 'Everyday use',
    'dcg': 'Durable',
}
banner = list(banner_lex.values())
rows = [
    ['2019.6', 100, 99.7, 104.5, 97.9, 100, 100.9, 102.2, 101.6, 100.5, 99.1],
    ['2019.5', 100.6, 100.6, 106.1, 99.4, 100.5, 100.9, 102.2, 101.5, 100.4, 99.2],
    ['2019.4', 100.9, 100.9, 105.3, 100, 100.9, 100.9, 101.9, 101.7, 100.3, 99.4],
    ['2019.3', 100.4, 100.3, 104.2, 99.4, 100.4, 100.5, 101.2, 101.7, 100.3, 99.3],
    ['2019.2', 100.1, 99.9, 101.8, 98.5, 100.3, 100.4, 100.8, 101.6, 100.2, 99.4],
    ['2019.1', 100.1, 99.9, 101.2, 98.4, 100.3, 100.6, 100.8, 101.6, 100.3, 100],
    ['2018.12', 100.9, 101, 103.8, 100.8, 100.8, 100.7, 100.9, 101.6, 100.4, 100.2],
    ['2018.11', 102.7, 103.3, 109.2, 104.6, 102.2, 100.8, 101.1, 101.5, 100.8, 100.1],
    ['2018.1', 103.3, 104.2, 112.4, 106.7, 102.5, 100.7, 100.9, 101.2, 101, 99.9],
    ['2018.9', 103.6, 104.6, 111.7, 107.3, 102.9, 100.8, 100.9, 101.1, 101.1, 100.2],
    ['2018.8', 104.1, 105.2, 112.1, 107.8, 103.5, 100.7, 100.7, 101.1, 101.2, 100.2],
    ['2018.7', 104.6, 106, 113.4, 109, 104.1, 100.6, 100.7, 100.7, 101.1, 99.8],
    ['2018.6', 104.7, 106.1, 111.5, 108.8, 104.6, 100.4, 100.7, 100.3, 101.1, 99.5],
    ['2018.5', 104.1, 105.4, 108.1, 107.4, 104.4, 100.3, 100.3, 100.3, 101.1, 99.3],
    ['2018.4', 103.4, 104.5, 106.1, 105.7, 103.9, 100.1, 100.1, 100.2, 100.9, 99.4],
    ['2018.3', 103.1, 104.1, 105, 105.1, 103.7, 100.2, 100, 100.3, 100.9, 99.7],
    ['2018.2', 103.7, 104.8, 106.4, 105.9, 104.2, 100.3, 100, 100.5, 101.1, 99.9],
    ['2018.1', 104.3, 105.7, 106.8, 107.3, 104.9, 100.3, 100, 100.8, 101.4, 99.7],
    ['2017.12', 106.3, 106.4, 120.67, 111.53, 106.09, 100.65, 100.6, 101.16, 101.32, 99.88],
    ['2017.11', 105.8, 107.5, 110.8, 109.7, 106.3, 100.6, 100.4, 100.7, 101.7, 100],
    ['2017.1', 106.9, 109, 114.7, 111.6, 107.5, 100.8, 100.6, 100.9, 101.9, 100],
    ['2017.9', 106.9, 109.1, 117.2, 111.9, 107.3, 100.7, 100.7, 101.2, 101.3, 100],
    ['2017.8', 106.4, 108.3, 118.2, 111, 106.4, 100.6, 100.7, 101.4, 100.8, 100],
    ['2017.7', 105.5, 107.3, 115.8, 109.3, 105.8, 100.5, 100.4, 101.2, 100.6, 100],
    ['2017.6', 105.5, 107.3, 118.3, 110, 105.4, 100.5, 100.1, 101.3, 101, 100.1],
    ['2017.5', 101, 107.3, 122.7, 111.1, 104.6, 100.6, 100.3, 101.5, 101.1, 100.2],
    ['2017.4', 101.4, 108.4, 128.3, 113, 105.2, 100.7, 100.5, 101.5, 101.4, 99.9],
    ['2017.3', 107.6, 110.1, 133.7, 114.9, 106.5, 100.7, 100.7, 101.3, 101.4, 99.6],
    ['2017.2', 107.8, 110.4, 136.1, 115.5, 106.6, 100.8, 101.1, 101.3, 101.5, 99.4],
    ['2017.1', 106.9, 109.1, 131, 112.9, 105.9, 100.8, 101.3, 101.1, 101.5, 99.4],
    ['2016.12', 98.63, 107.2, 95.4, 96.72, 98.97, 99.96, 100.55, 100.88, 100.04, 98.55],
    ['2016.11', 103.3, 104.3, 114.8, 105.8, 102.9, 100.4, 100.9, 101.1, 100.7, 99],
    ['2016.1', 101.2, 101.6, 107.9, 101.9, 100.9, 100.1, 100.6, 100.9, 100.2, 98.8],
    ['2016.9', 100.1, 100.1, 102.1, 99.8, 100.1, 100, 100.3, 100.7, 100.5, 98.5],
    ['2016.8', 99.2, 99, 96.8, 97.7, 99.6, 100, 100.1, 100.8, 100.7, 98.7],
    ['2016.7', 98.3, 97.7, 94.4, 95.5, 98.8, 100, 100.2, 101.1, 100.6, 98.6],
]
