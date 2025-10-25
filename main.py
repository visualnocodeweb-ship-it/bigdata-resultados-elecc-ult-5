import pandas as pd
import json

def excel_to_json_2021(excel_file, json_file):
    try:
        df = pd.read_excel(excel_file, engine='openpyxl')
        df.rename(columns={
            'CAMBIA NEUQUÃ_x0089_N': 'CAMBIA NEUQUAN',
            'COALICIÃ_x0093_N CÃ_x008d_VICA - AFIRMACIÃ_x0093_N PARA UNA REPÃ_x009a_BLICA IGUALITARIA (ARI)': 'COALICION CIVICA - ARI',
            'FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD': 'FRENTE DE IZQUIERDA',
            'MOVIMIENTO LIBRES DEL SUR': 'LIBRES DEL SUR',
            'MOVIMIENTO POPULAR NEUQUINO': 'MPN',
            'SOCIALISTA': 'SOCIALISTA',
            'undefined': 'INDEFINIDO',
            'TOTAL VOTOS': 'TOTAL'
        }, inplace=True)
        columnas_partidos = ['CAMBIA NEUQUAN', 'COALICION CIVICA - ARI', 'FRENTE DE IZQUIERDA', 'FRENTE DE TODOS', 'LIBRES DEL SUR', 'MPN', 'SOCIALISTA', 'INDEFINIDO', 'TOTAL']
        df['mesa_id'] = df['mesa_id'].fillna(0).astype(int)
        df_agrupado = df.groupby('mesa_id')[columnas_partidos].sum().to_dict(orient='index')
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(df_agrupado, f, ensure_ascii=False, indent=4)
        print(f"El archivo {json_file} se ha creado correctamente.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {excel_file}")
    except Exception as e:
        print(f"Ocurrió un error al procesar {excel_file}: {e}")

def excel_to_json_2013(excel_file, json_file):
    try:
        df = pd.read_excel(excel_file, engine='openpyxl')
        partidos = ['COMPROMISO CIVICO NEUQUINO', 'FRENTE DE IZQUIERDA Y DE LOS TRABAJADORES', 'FRENTE PARA LA VICTORIA', 'FRENTE PROGRESISTA SUR', 'MOVIMIENTO LIBRES DEL SUR', 'MOVIMIENTO POPULAR NEUQUINO', 'UNION DE LOS NEUQUINOS', 'UNION POPULAR']
        for partido in partidos:
            df[partido] = df[f'DIPUTADO NACIONAL_{partido}_POSITIVO'] + df[f'SENADOR NACIONAL_{partido}_POSITIVO']
        df['mesa_id'] = df['mesa_id'].fillna(0).astype(int)
        df_agrupado = df.groupby('mesa_id')[partidos].sum().to_dict(orient='index')
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(df_agrupado, f, ensure_ascii=False, indent=4)
        print(f"El archivo {json_file} se ha creado correctamente.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {excel_file}")
    except Exception as e:
        print(f"Ocurrió un error al procesar {excel_file}: {e}")

def excel_to_json_2017(excel_file, json_file):
    try:
        df = pd.read_excel(excel_file, engine='openpyxl')
        df.rename(columns={
            'mesa_id__': 'mesa_id',
            'DIPUTADO NACIONAL_1PAIS FRENTE RENOVADOR NEUQUEN +A_POSITIVO': '1PAIS FRENTE RENOVADOR',
            'DIPUTADO NACIONAL_CAMBIEMOS_POSITIVO': 'CAMBIEMOS',
            'DIPUTADO NACIONAL_FRENTE DE IZQUIERDA Y DE LOS TRABAJADORES_POSITIVO': 'FRENTE DE IZQUIERDA',
            'DIPUTADO NACIONAL_FRENTE NEUQUINO_POSITIVO': 'FRENTE NEUQUINO',
            'DIPUTADO NACIONAL_MOVIMIENTO LIBRES DEL SUR_POSITIVO': 'LIBRES DEL SUR',
            'DIPUTADO NACIONAL_MOVIMIENTO POPULAR NEUQUINO_POSITIVO': 'MPN',
            'DIPUTADO NACIONAL_NUEVA IZQUIERDA_POSITIVO': 'NUEVA IZQUIERDA',
            'DIPUTADO NACIONAL_UNIDAD CIUDADANA PARA LA VICTORIA_POSITIVO': 'UNIDAD CIUDADANA'
        }, inplace=True)
        columnas_partidos = ['1PAIS FRENTE RENOVADOR', 'CAMBIEMOS', 'FRENTE DE IZQUIERDA', 'FRENTE NEUQUINO', 'LIBRES DEL SUR', 'MPN', 'NUEVA IZQUIERDA', 'UNIDAD CIUDADANA']
        df['mesa_id'] = df['mesa_id'].fillna(0).astype(int)
        df_agrupado = df.groupby('mesa_id')[columnas_partidos].sum().to_dict(orient='index')
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(df_agrupado, f, ensure_ascii=False, indent=4)
        print(f"El archivo {json_file} se ha creado correctamente.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {excel_file}")
    except Exception as e:
        print(f"Ocurrió un error al procesar {excel_file}: {e}")

def excel_to_json_paso_2021(excel_file, json_file):
    try:
        df = pd.read_excel(excel_file, engine='openpyxl')
        df.rename(columns={
            'CAMBIA NEUQUÃ_x0089_N - POSITIVO': 'CAMBIA NEUQUAN',
            'COALICIÃ_x0093_N CÃ_x008d_VICA - AFIRMACIÃ_x0093_N PARA UNA REPÃ_x009a_BLICA IGUALITARIA (ARI) - POSITIVO': 'COALICION CIVICA - ARI',
            'FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD - POSITIVO': 'FRENTE DE IZQUIERDA',
            'FRENTE DE TODOS - POSITIVO': 'FRENTE DE TODOS',
            'MOVIMIENTO AL SOCIALISMO - POSITIVO': 'MOVIMIENTO AL SOCIALISMO',
            'MOVIMIENTO LIBRES DEL SUR - POSITIVO': 'LIBRES DEL SUR',
            'MOVIMIENTO POPULAR NEUQUINO - POSITIVO': 'MPN',
            'SOCIALISTA - POSITIVO': 'SOCIALISTA'
        }, inplace=True)
        columnas_partidos = ['CAMBIA NEUQUAN', 'COALICION CIVICA - ARI', 'FRENTE DE IZQUIERDA', 'FRENTE DE TODOS', 'MOVIMIENTO AL SOCIALISMO', 'LIBRES DEL SUR', 'MPN', 'SOCIALISTA']
        df['mesa_id'] = df['mesa_id'].fillna(0).astype(int)
        df_agrupado = df.groupby('mesa_id')[columnas_partidos].sum().to_dict(orient='index')
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(df_agrupado, f, ensure_ascii=False, indent=4)
        print(f"El archivo {json_file} se ha creado correctamente.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {excel_file}")
    except Exception as e:
        print(f"Ocurrió un error al procesar {excel_file}: {e}")

def excel_to_json_2023(excel_file, json_file):
    try:
        df = pd.read_excel(excel_file, engine='openpyxl')
        columnas_partidos = ['ARRIBA NEUQUEN (LLA)', 'JUNTOS POR EL CAMBIO', 'UNION POR LA PATRIA', 'FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD', 'MOVIMIENTO POPULAR NEUQUINO']
        df['Mesa'] = df['Mesa'].fillna(0).astype(int)
        df_agrupado = df.groupby('Mesa')[columnas_partidos].sum().to_dict(orient='index')
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(df_agrupado, f, ensure_ascii=False, indent=4)
        print(f"El archivo {json_file} se ha creado correctamente.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {excel_file}")
    except Exception as e:
        print(f"Ocurrió un error al procesar {excel_file}: {e}")

def aggregate_election_data():
    try:
        # Read all excel files
        df_2021 = pd.read_excel('GENERALES DIPUTADOS 2021.xlsx', engine='openpyxl')
        df_2013 = pd.read_excel('GENERALES DIP-SEN 2013.xlsx', engine='openpyxl')
        df_2017 = pd.read_excel('GENERALES DIP 2017.xlsx', engine='openpyxl')
        df_paso_2021 = pd.read_excel('DIPUTADOS PASO 2021.xlsx', engine='openpyxl')
        df_2023 = pd.read_excel('DIPUTADOS 2023.xlsx', engine='openpyxl')

        # Process 2021 data
        df_2021.rename(columns={
            'CAMBIA NEUQUÃ_x0089_N': 'CAMBIA NEUQUAN',
            'COALICIÃ_x0093_N CÃ_x008d_VICA - AFIRMACIÃ_x0093_N PARA UNA REPÃ_x009a_BLICA IGUALITARIA (ARI)': 'COALICION CIVICA - ARI',
            'FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD': 'FRENTE DE IZQUIERDA',
            'MOVIMIENTO LIBRES DEL SUR': 'LIBRES DEL SUR',
            'MOVIMIENTO POPULAR NEUQUINO': 'MPN',
            'SOCIALISTA': 'SOCIALISTA',
            'undefined': 'INDEFINIDO',
            'TOTAL VOTOS': 'TOTAL'
        }, inplace=True)
        df_2021['year'] = 2021
        df_2021_melted = df_2021.melt(id_vars=['mesa_id', 'year'], value_vars=['CAMBIA NEUQUAN', 'COALICION CIVICA - ARI', 'FRENTE DE IZQUIERDA', 'FRENTE DE TODOS', 'LIBRES DEL SUR', 'MPN', 'SOCIALISTA'], var_name='party', value_name='votes')

        # Process 2013 data
        partidos_2013 = ['COMPROMISO CIVICO NEUQUINO', 'FRENTE DE IZQUIERDA Y DE LOS TRABAJADORES', 'FRENTE PARA LA VICTORIA', 'FRENTE PROGRESISTA SUR', 'MOVIMIENTO LIBRES DEL SUR', 'MOVIMIENTO POPULAR NEUQUINO', 'UNION DE LOS NEUQUINOS', 'UNION POPULAR']
        for partido in partidos_2013:
            df_2013[partido] = df_2013[f'DIPUTADO NACIONAL_{partido}_POSITIVO'] + df_2013[f'SENADOR NACIONAL_{partido}_POSITIVO']
        df_2013['year'] = 2013
        df_2013_melted = df_2013.melt(id_vars=['mesa_id', 'year'], value_vars=partidos_2013, var_name='party', value_name='votes')

        # Process 2017 data
        df_2017.rename(columns={
            'mesa_id__': 'mesa_id',
            'DIPUTADO NACIONAL_1PAIS FRENTE RENOVADOR NEUQUEN +A_POSITIVO': '1PAIS FRENTE RENOVADOR',
            'DIPUTADO NACIONAL_CAMBIEMOS_POSITIVO': 'CAMBIEMOS',
            'DIPUTADO NACIONAL_FRENTE DE IZQUIERDA Y DE LOS TRABAJADORES_POSITIVO': 'FRENTE DE IZQUIERDA',
            'DIPUTADO NACIONAL_FRENTE NEUQUINO_POSITIVO': 'FRENTE NEUQUINO',
            'DIPUTADO NACIONAL_MOVIMIENTO LIBRES DEL SUR_POSITIVO': 'LIBRES DEL SUR',
            'DIPUTADO NACIONAL_MOVIMIENTO POPULAR NEUQUINO_POSITIVO': 'MPN',
            'DIPUTADO NACIONAL_NUEVA IZQUIERDA_POSITIVO': 'NUEVA IZQUIERDA',
            'DIPUTADO NACIONAL_UNIDAD CIUDADANA PARA LA VICTORIA_POSITIVO': 'UNIDAD CIUDADANA'
        }, inplace=True)
        df_2017['year'] = 2017
        df_2017_melted = df_2017.melt(id_vars=['mesa_id', 'year'], value_vars=['1PAIS FRENTE RENOVADOR', 'CAMBIEMOS', 'FRENTE DE IZQUIERDA', 'FRENTE NEUQUINO', 'LIBRES DEL SUR', 'MPN', 'NUEVA IZQUIERDA', 'UNIDAD CIUDADANA'], var_name='party', value_name='votes')

        # Process PASO 2021 data
        df_paso_2021.rename(columns={
            'CAMBIA NEUQUÃ_x0089_N - POSITIVO': 'CAMBIA NEUQUAN',
            'COALICIÃ_x0093_N CÃ_x008d_VICA - AFIRMACIÃ_x0093_N PARA UNA REPÃ_x009a_BLICA IGUALITARIA (ARI) - POSITIVO': 'COALICION CIVICA - ARI',
            'FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD - POSITIVO': 'FRENTE DE IZQUIERDA',
            'FRENTE DE TODOS - POSITIVO': 'FRENTE DE TODOS',
            'MOVIMIENTO AL SOCIALISMO - POSITIVO': 'MOVIMIENTO AL SOCIALISMO',
            'MOVIMIENTO LIBRES DEL SUR - POSITIVO': 'LIBRES DEL SUR',
            'MOVIMIENTO POPULAR NEUQUINO - POSITIVO': 'MPN',
            'SOCIALISTA - POSITIVO': 'SOCIALISTA'
        }, inplace=True)
        df_paso_2021['year'] = 'PASO 2021'
        df_paso_2021_melted = df_paso_2021.melt(id_vars=['mesa_id', 'year'], value_vars=['CAMBIA NEUQUAN', 'COALICION CIVICA - ARI', 'FRENTE DE IZQUIERDA', 'FRENTE DE TODOS', 'MOVIMIENTO AL SOCIALISMO', 'LIBRES DEL SUR', 'MPN', 'SOCIALISTA'], var_name='party', value_name='votes')

        # Process 2023 data
        df_2023.rename(columns={'Mesa': 'mesa_id'}, inplace=True)
        df_2023['year'] = 2023
        df_2023_melted = df_2023.melt(id_vars=['mesa_id', 'year'], value_vars=['ARRIBA NEUQUEN (LLA)', 'JUNTOS POR EL CAMBIO', 'UNION POR LA PATRIA', 'FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD', 'MOVIMIENTO POPULAR NEUQUINO'], var_name='party', value_name='votes')

        # Concatenate all dataframes
        all_data = pd.concat([df_2021_melted, df_2013_melted, df_2017_melted, df_paso_2021_melted, df_2023_melted])
        all_data['mesa_id'] = all_data['mesa_id'].fillna(0).astype(int)

        # Create the aggregated structure
        aggregated_data = {}
        for mesa_id, mesa_df in all_data.groupby('mesa_id'):
            mesa_data = {'years': {},'total_votes': int(mesa_df['votes'].sum())}
            for year, year_df in mesa_df.groupby('year'):
                year_data = year_df.set_index('party')['votes'].to_dict()
                for party, votes in year_data.items():
                    year_data[party] = int(votes)
                mesa_data['years'][year] = year_data
            aggregated_data[mesa_id] = mesa_data

        with open('aggregated_data.json', 'w', encoding='utf-8') as f:
            json.dump(aggregated_data, f, ensure_ascii=False, indent=4)

        print("El archivo aggregated_data.json se ha creado correctamente.")

    except FileNotFoundError as e:
        print(f"Error: No se encontró el archivo {e.filename}")
    except Exception as e:
        print(f"Ocurrió un error al agregar los datos: {e}")

if __name__ == '__main__':
    excel_to_json_2021('GENERALES DIPUTADOS 2021.xlsx', 'data.json')
    excel_to_json_2013('GENERALES DIP-SEN 2013.xlsx', 'data_2013.json')
    excel_to_json_2017('GENERALES DIP 2017.xlsx', 'data_2017.json')
    excel_to_json_paso_2021('DIPUTADOS PASO 2021.xlsx', 'data_paso_2021.json')
    excel_to_json_2023('DIPUTADOS 2023.xlsx', 'data_2023.json')
    aggregate_election_data()