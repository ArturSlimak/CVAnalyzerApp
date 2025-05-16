from concurrent import futures
import grpc
import generated.analyzer_pb2 as analyzer_pb2
import generated.analyzer_pb2_grpc as analyzer_pb2_grpc

from app.services.grammar_analyzer import check_grammar
from app.services.file_extractors.extractor_factory import get_extractor


class ResumeAnalyzerService(analyzer_pb2_grpc.ResumeAnalyzerServicer):
    def AnalyzePDF(self, request, context):

        try:
            extractor = get_extractor(request.file_type)
            extracted_text = extractor.extract_text(request.file)

            if not extracted_text.strip():
                context.abort(grpc.StatusCode.INVALID_ARGUMENT,
                              "File contains no extractable text.")

            grammar_issues = check_grammar(extracted_text)

            grammar_issues_proto = [
                analyzer_pb2.GrammarIssue(
                    message=issue.message,
                    context=issue.context,
                    offset=issue.offset,
                    length=issue.length,
                    replacement=issue.replacement
                ) for issue in grammar_issues
            ]

            return analyzer_pb2.AnalyzeResponse(
                grammar_feedback=grammar_issues_proto,
                extracted_text=extracted_text
            )

        except grpc.RpcError as rpc_error:
            raise rpc_error
        except Exception as e:
            context.abort(grpc.StatusCode.UNKNOWN, f"Server error: {str(e)}")
