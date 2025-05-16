import grpc
from dotenv import load_dotenv
from concurrent import futures
from generated import analyzer_pb2_grpc
from app.services.analyzer_service import ResumeAnalyzerService
from app.utils.logging_config import setup_logger

load_dotenv()
logger = setup_logger(__name__)


def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    analyzer_pb2_grpc.add_ResumeAnalyzerServicer_to_server(
        ResumeAnalyzerService(), server)
    server.add_insecure_port('[::]:50051')

    logger.info("Analyzer service running on port 50051...")

    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
