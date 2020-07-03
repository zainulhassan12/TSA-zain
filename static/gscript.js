var selected;
var json = {};
var SelectedAnswer = [];
var clickcheck = null;
var selvalue;
var valueofselection;
var check = false;
var selctedanswer =[];
var ch;
var ques;
var ans;
for( var i=0;i<ques.length; i++)
{
			var para = document.createElement("p");
            var btn =document.createElement("button");btn.innerHTML="Submit";btn.type='button';btn.className="btn btn-outline-success";btn.id="b1";
			btn.setAttribute("onclick", "RadioFun()")
			var node = document.createTextNode(ques[i]['question']);
			para.appendChild(node);
            var newline = document.createElement('br');
            var co = document.getElementById("z");
			co.style="margin:10px";
            //var form = document.getElementById("form1");
            co.appendChild(para); var olist = document.createElement('ul');
                          olist.id="Answerlist";
	    for (var n=0;n<ans.length;n++)
	    {
			  if(ans[n]['question_id']==ques[i]['id'])
			 {
						 var line = document.createElement('br');
						 var radio = document.createElement('input');
						 radio.type = "radio";
						 radio.name ="choice"+i;
                          radio.id = "radio";
			              radio.value =ans[n]['answer'];
						  var label = document.createElement('label')
						  label.htmlFor = 'contact';
						  var description = document.createTextNode(""+ans[n]['answer']);
			              label.appendChild(description);
//                          var olist = document.getElementById('list1');

                          var ilist = document.createElement('li');
                          ilist.id="option";
                          ilist.setAttribute("onclick","fun(this)");
                          ilist.setAttribute("style",";");
						  ilist.appendChild(radio);
						  ilist.appendChild(label);
						  olist.append(ilist);

			}
			co.append(olist);
	    }
 }

function fun(a){
selvalue=a.closest('li').lastChild.innerHTML;
console.log(selvalue);

}
$("#b1").click(function()
{
});
co.appendChild(btn);


function RadioFun(){
var j= 0;
for (var i =0;i<ques.length; i++)
{
var c = "choice"+i;
var radios = document.getElementsByName(c);
	   for(var k =0;k<radios.length;k++)
		{
			if(radios[k].checked)
			{
				var s = radios[k].value;
				//console.log(s + "|radio");
			}
		}
	    if (s != null)
	    {
			j=j+1;
			console.log(j);
			s = null;
		}
}

	 if (j<ques.length)
		{
			alert("Please Select Answer For Each Question");
		}
     else
		{
		 for (var i=0;i<ques.length; i++)
			{
				var c = "choice"+i;
				var radios = document.getElementsByName(c);
				  for(var k =0;k<radios.length;k++)
					{
						if(radios[k].checked)
						{
							var z = radios[k].value;
							json.question_id= ques[i]['id'];
							json.question = ques[i]['question'];
							json.answer = z;
							SelectedAnswer.push(json);
							//console.log(ques[i]['question']);
						}
					}
	        }
		 }
console.log(SelectedAnswer);
}
