$(document).ready(function () {
  $("#quiz-button").hide();
  let questionsToAsk = [
    "Which is your happy place?",
    "Do you like it hot - or not?",
    "Do you love romance or long for adventure?",
    "Are you a culture vulture or do you love to explore?",
  ];
  let answers = [
    "The countryside",
    "The city",
    "Sandy beaches",
    "Snowy landscapes",
    "Going on safari",
    "Croissants in Paris",
    "Bring me the horizon",
    "Give me history",
  ];
  let keywords = [
    "nature",
    "city",
    "summer",
    "winter",
    "adventure",
    "romantic",
    "exotic",
    "culture",
  ];
  let text = "";
  let i = 0;
  let j = 0;
  let k = 1;
  let question = $(".quiz-question");
  let answerOne = $("#answerOne");
  let answerTwo = $("#answerTwo");
  question.text(questionsToAsk[i]);
  answerOne.text(answers[j]);
  answerTwo.text(answers[k]);
  answerOne.on("click", function () {
    if (i < 3) {
      question.fadeOut(1000, function () {
        question.text(questionsToAsk[i]).fadeIn(1000);
      });
      answerOne.fadeOut(1000, function () {
        answerOne.text(answers[j]).fadeIn(1000);
      });
      answerTwo.fadeOut(1000, function () {
        answerTwo.text(answers[k]).fadeIn(1000);
      });
      text += keywords[j] + " ";
      $("#results").val(text);
      i++;
      j += 2;
      k += 2;
    } else if (i == 3) {
      text += keywords[j] + " ";
      $("#results").val(text);
      answerOne.fadeOut(1000);
      answerTwo.fadeOut(1000);
      $("#quiz-button").delay(1500).fadeIn(500);
      $("#quiz-button").prop("type", "submit");
    }
    console.log(text);
  });
  answerTwo.on("click", function () {
    if (i < 3) {
      question.fadeOut(1000, function () {
        question.text(questionsToAsk[i]).fadeIn(1000);
      });
      answerOne.fadeOut(1000, function () {
        answerOne.text(answers[j]).fadeIn(1000);
      });
      answerTwo.fadeOut(1000, function () {
        answerTwo.text(answers[k]).fadeIn(1000);
      });
      text += keywords[k] + " ";
      $("#results").val(text);
      i++;
      j += 2;
      k += 2;
    } else if (i == 3) {
      text += keywords[k] + " ";
      $("#results").val(text);
      answerOne.fadeOut(1000);
      answerTwo.fadeOut(1000);
      $("#quiz-button").delay(1500).fadeIn(500);
      $("#quiz-button").prop("type", "submit");
    }
    console.log(text);
  });
});
