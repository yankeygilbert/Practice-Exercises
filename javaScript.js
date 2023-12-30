var ask = (question,yes,no) => confirm(question)? yes(): no();
ask("do you agree",()=> alert("you agreed"),()=>"you cancelled request");