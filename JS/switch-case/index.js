const date = new Date();

const days = ["sun", "mon", "tue", "wed", "thr", "fri", "sat"];

// console.log(days[new Date().getDay()]);

// console.log(typeof date);
// console.log(days[date.getDay()]);

// switch (date.getDay()) {
//   case 0:
//     console.log(days[0]);
//     break;
//   case 1:
//     console.log(days[1]);
//     break;
//   case 2:
//     console.log(days[2]);
//     break;
//   case 3:
//     console.log(days[3]);
//     break;
//   case 4:
//     console.log(days[4]);
//     break;
//   case 5:
//     console.log(days[5]);
//     break;
//   case 6:
//     console.log(days[6]);
//     break;

//   default:
//     console.log("inavlid");
//     break;
// }

// console.log(typeof Date());
// console.log(typeof new Date());
// console.log(new Date().getDay());

switch (new Date().getDay()) {
  case 0:
    console.log("sun");
    break;

  case 1:
    console.log("mon");
    break;

  case 2:
    console.log("tue");
    break;

  case 3:
    console.log("wed");
    break;

  case 4:
    console.log("thr");
    break;

  case 5:
    console.log("fri");
    break;

  case 6:
    console.log("sat");
    break;

  default:
    console.log("invalid");
    break;
}
