url="http://35.193.45.56/sparta/"
source code="""< script >
    var items = ["value", "user", "getElementById", "pass", "Cyber-Talent", "Congratz \x0A\x0A", "wrong Password"];

function check() {
    var correct = document[items[2]](items[1])[items[0]];
    var success = document[items[2]](items[3])[items[0]];

    if (correct == items[4] && success == items[4]) {
        alert(items[5]);
    } else {
        alert(items[6]);
    }
} <
/script>"""

#This challenge is testing of javascript deobfuscation
# FLAG: {J4V4_Scr1Pt_1S_Aw3s0me}