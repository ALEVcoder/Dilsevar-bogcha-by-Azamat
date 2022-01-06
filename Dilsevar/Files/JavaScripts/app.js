const counters = document.querySelectorAll('.counter')
const speed = 9000000;

counters.forEach(counter =>{
    const updataCount = ()=>{
        const target = +counter.getAttribute('data-target')
        const count = +counter.innerText

        const inc = target / speed

        if(count<target){
            counter.innerText = Math.ceil(count + inc);
            setTimeout(updataCount,100)
        }else{
            count.innerText = target
        }
    }
    updataCount()
})  

// document.querySelector('#menuni').addEventListener("click", function () {
//     console.log("hello");
//     document.querySelector('.ul').style.right= "0";
// });

// document.querySelector('#yop').addEventListener("click", function () {
//     document.querySelector('.ul').style.left = "30rem";
// });
