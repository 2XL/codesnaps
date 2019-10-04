let day_limit = 100;

let hour_limit = 20;

// open the developer terminal, scroll some possible followers

function getRandomArbitrary(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}

function getRandomListSize(size, min, max) {

    let list_itv_hit = {};
    for (let i = 0; i < size; i++) {
        let rand_val = getRandomArbitrary(min, max);
        if (rand_val in list_itv_hit) {
            list_itv_hit[rand_val] += 1
        } else {
            list_itv_hit[rand_val] = 1
        }
    }
    return list_itv_hit;
}


let follow_time_hit = getRandomListSize();

// random follow, 20 persons in random interval in one hour
function follow_hour(hour_limit, follow_time_hit) {
    // get followers button list
    let follow_buttons = document.getElementsByTagName("button");
    // get following interval

    let follow_buttons_idx = 0;
    let follow_buttons_clicked = 0;
    let time_idx = 0;

    while (follow_buttons_clicked < hour_limit) {
        if (time_idx in follow_time_hit) {
            while (follow_time_hit[time_idx] > 0) {
                if (follow_buttons[follow_buttons_idx++].textContent === "Seguir") {
                    console.log("Seguir");
                    // follow_buttons[follow_buttons_idx].click();
                    follow_buttons[follow_buttons_idx].textContent;

                    follow_time_hit[time_idx]--;
                    follow_buttons_clicked++;
                }
            }

        }
        let itv = setInterval(function () {


        }, delay_time);

    }
}

// generate 6 random in between 60
function getNextFollowButton() {

}

let delay_time = 1000;

let itv_idx = 0;
let follow_idx = 0;


