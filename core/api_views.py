from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer


class QuestionListView(APIView):
    def get(self, request, *args, **kwargs):
        questions = Question.objects.all()
        serializers_data = QuestionSerializer(instance=questions, many=True).data
        return Response(serializers_data, status=status.HTTP_200_OK)



class QuestionCreateView(APIView):
    def post(self, request, *args, **kwargs):
        data = QuestionSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_200_OK)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    def put(self, request, pk):
        questions = Question.objects.get(pk=pk)
        serializer_data = QuestionSerializer(instance=questions, data=request.data, partial=True)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data, status=status.HTTP_200_OK)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    def delete(self, request, pk):
        questions = Question.objects.get(pk=pk)
        questions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnswerCreateView(APIView):
    def post(self, request):
        answer = AnswerSerializer(data=request.data)
        if answer.is_valid():
            answer.save()
            return Response(answer.data, status=status.HTTP_200_OK)
        return Response(answer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerUpdateView(APIView):
    def put(self, request, pk):
        answer = Answer.objetcs.get(pk=pk)
        data = AnswerSerializer(instance=answer, data=request.data, partial=True)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_200_OK)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerDeleteView(APIView):
    def delete(self, request, pk):
        answer = Answer.objects.get(pk=pk)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)