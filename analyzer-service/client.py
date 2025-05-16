import grpc
import generated.analyzer_pb2 as analyzer_pb2
import generated.analyzer_pb2_grpc as analyzer_pb2_grpc


def load_pdf_bytes(path: str) -> bytes:
    with open(path, "rb") as f:
        return f.read()


def main():
    # Connect to gRPC server
    channel = grpc.insecure_channel('localhost:50051')
    stub = analyzer_pb2_grpc.ResumeAnalyzerStub(channel)

    # Prepare request
    pdf_bytes = load_pdf_bytes("sample_resume.pdf")

    request = analyzer_pb2.AnalyzePDFRequest(
        file=pdf_bytes,
        file_type="pdf"
    )

    # Call gRPC method
    response = stub.AnalyzePDF(request)

    # Print the results
    print("=== gRPC Response ===")
    print("Grammar Feedback:", response.grammar_feedback)
    print("Extracted Text (Preview):", response.extracted_text)


if __name__ == "__main__":
    main()
