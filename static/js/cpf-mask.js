

function formatCpfCnpj(value) {
  const digits = value.replace(/\D/g, "");

  if (digits.length <= 11) {
    return digits
      .replace(/(\d{3})(\d)/, "$1.$2")
      .replace(/(\d{3})(\d)/, "$1.$2")
      .replace(/(\d{3})(\d{1,2})$/, "$1-$2");
  } else {
    return digits
      .replace(/(\d{2})(\d)/, "$1.$2")
      .replace(/(\d{3})(\d)/, "$1.$2")
      .replace(/(\d{3})(\d)/, "$1.$2")
      .replace(/(\d{4})(\d{1,2})/, "$1-$2");
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector('form');
  const input = document.querySelector("cpf-cnpj-mask");

  if (form && input) {
    form.addEventListener('submit', function () {
      input.value = formatCpfCnpj(input.value);
    });
  }
});





/* function applyMask(value, pattern) {
  let i = 0;
  return pattern.replace(/#/g, () => value[i++] || '');
}

document.addEventListener('DOMContentLoaded', function () {
  const maskFields = [
      { selector: '.cpf-mask', pattern: '###.###.###-##', maxLength: 11 },
      { selector: '.cnpj-mask', pattern: '##.###.###/####-##', maxLength: 14 },
      { selector: '.phone-mask', pattern: '(##) #####-####', maxLength: 11 },
  ];

  maskFields.forEach(({ selector, pattern, maxLength }) => {
      const inputs = document.querySelectorAll(selector);
      inputs.forEach(input => {
          input.addEventListener('input', e => {
              let value = e.target.value.replace(/\D/g, '').slice(0, maxLength);
              e.target.value = applyMask(value, pattern);
          });
      });
  });
}); */





/* document.addEventListener("DOMContentLoaded", function () {

  const cpfFields = document.querySelectorAll(".cpf-mask");

  cpfFields.forEach(function (input) {
    input.addEventListener('input', function (e) {
      let value = e.target.value.replace(/\D/g, '');
      value = value.slice(0, 11);

      if (value.length > 9) {
        value = value.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4");
      } else if (value.length > 6) {
        value = value.replace(/(\d{3})(\d{3})(\d{1, 3})/, "$1.$2.$3");
      } else if (value.length > 3) {
        value = value.replace(/(\d{3})(\d{1, 3})/, "$1.$2");
      }

      e.target.value = value
    });

  });

}); */
