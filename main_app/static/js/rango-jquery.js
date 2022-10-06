$(document).ready(function() {

let questionsToAsk = ["Which is your happy place?", "Do you like it hot - or not?", "Do you love romance or long for adventure?", "Are you a culture vulture or do you love to explore?"];
let answers = ["The countryside", "The city", "Sandy beaches", "Snowy landscapes", "Going on safari", "Croissants in Paris", "Bring me the horizon", "Give me history"]
let keywords = ["nature", "city", "summer", "winter", "adventure", "romantic", "exotic", "culture"];
let questionsAnswered = [];
let i = 0;
let j = 0;
let k = 1;
let question = $(".quiz-question");
let answerOne = $('#answerOne');
let answerTwo = $('#answerTwo');
question.text(questionsToAsk[i]);
answerOne.text(answers[i]);
answerTwo.text(answers[i + 1]);
answerOne.on("click", function() {
    question.fadeOut(2000, function() {
        question.text(questionsToAsk[i]).fadeIn(2000);
    });
    answerOne.fadeOut(2000, function() {
        answerOne.text(answers[j]).fadeIn(2000);
    });
    answerTwo.fadeOut(2000, function() {
        answerTwo.text(answers[k]).fadeIn(2000);
    });
    questionsAnswered.push(keywords[j]);
    i++;
    j += 2;
    k += 2;
    console.log(questionsAnswered);
});
answerTwo.on("click", function() {
    question.fadeOut(2000, function() {
        question.text(questionsToAsk[i]).fadeIn(2000);
    });
    answerOne.fadeOut(2000, function() {
        answerOne.text(answers[j]).fadeIn(2000);
    });
    answerTwo.fadeOut(2000, function() {
        answerTwo.text(answers[k]).fadeIn(2000);
    });
    questionsAnswered.push(keywords[k]);
    i++;
    j += 2;
    k += 2;
    console.log(questionsAnswered)
});

});

