$(document).ready(function() {

let questionsToAsk = ["Which is your happy place?", "Do you like it hot - or not?", "Do you love romance or long for adventure?", "Are you a culture vulture or do you love to explore?"];
let answers = ["The city", "The countryside", "Sandy beaches", "Snowy landscapes"]
let keywords = ["nature", "city", "summer", "winter", "adventure", "romantic", "exotic", "culture"];
let questionsAnswered = [];
let question = $(".quiz-question");
let answerOne = $('#answerOne');
let answerTwo = $('#answerTwo');
question.text(questionsToAsk[0]);
answerOne.text(answers[0]);
answerTwo.text(answers[1]);
answerOne.on("click", function() {
    question.fadeOut(2000, function() {
        question.text(questionsToAsk[1]).fadeIn(2000);
    });
    answerOne.fadeOut(2000, function() {
        answerOne.text(answers[2]).fadeIn(2000);
    });
    answerTwo.fadeOut(2000, function() {
        answerTwo.text(answers[3]).fadeIn(2000);
    });
})
});
