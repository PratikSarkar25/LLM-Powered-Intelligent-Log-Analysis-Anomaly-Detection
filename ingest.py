# from parser import load_logs
# from rag_engine import build_index

# if __name__ == '__main__':
#     df = load_logs()
#     build_index(df)
#     print('Index built successfully')



from parser import load_logs
from rag_engine import build_index
from anomaly import detect_anomalies


def main():

    print('Loading logs...')
    df = load_logs()

    print(f'Total logs loaded: {len(df)}')

    print('Running anomaly detection...')
    anomalies = detect_anomalies(df)

    print('\nDetected Issues:')
    for issue in anomalies:
        print(f' - {issue}')

    print('\nBuilding vector index...')
    build_index(df)

    print('\n✅ Enterprise log ingestion completed successfully')


if __name__ == '__main__':
    main()
