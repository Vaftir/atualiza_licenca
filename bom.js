// //Evento no botão data de vencimento para calcular o prazo financeiro.
// $('#vencimento').getControl().change(function(){
//     calcularPrazoFinanceiro();
    
//   });
  
//   //Evento no botão data de vencimento para calcular o prazo financeiro.
//   $('#vencimento').getControl().blur(function(){
//     calcularPrazoFinanceiro();
//   });
  
//   //Evento no botão data de fora do prazo fiscal para calcular o prazo financeiro.
//   $('#fora_prz_fiscal').getControl().blur( function () {
//     calcularPrazoFinanceiro();
//   });
  
  
//   function calcularPrazoFinanceiro(){
//    var PrazoFinanceiro = 5;//Quantidade de dias informado pela controladoria 
   
//    var dataVencimentoBoleto = $("#vencimento").getValue();//retorna: 2023-08-30 00:00:00
//    dataVencimentoBoleto = formatarDataAmericano(dataVencimentoBoleto);//retorna: 2023/08/25
//    dataVencimentoBoleto = new Date(dataVencimentoBoleto);
   
//    var dataPrevistaPagamento = prazoFinanceiroDiasUteis(PrazoFinanceiro); 
//    console.log("Data de aprovação + 5 dias úteis: " + formatarDataBrasil(dataPrevistaPagamento));
    
//    var diferecaDias = parseInt(calculo(dataPrevistaPagamento, dataVencimentoBoleto));
//    console.log("Data Vencimento: " + formatarDataBrasil(dataVencimentoBoleto) + " - " + "Data de aprovação: " + formatarDataBrasil(new Date()) + " + 5 dias úteis: " + formatarDataBrasil(dataPrevistaPagamento) + " = " + diferecaDias + " dias.");
    
//   //Sistema irá calcular o prazo financeiro quando não estiver fora e irá setar o valor 1 - SIM e 2 - NÃO.
//     if(diferecaDias < 5){
//       $("#fora_prz_fin").setValue(1);
//       $('#obsforaPrazoFinanceiro').enableValidation();
//     }else if(diferecaDias >= 5){
//       $("#fora_prz_fin").setValue(2);
//       $('#obsforaPrazoFinanceiro').disableValidation();    
//     }
//   }  
  
//   function prazoFinanceiroDiasUteis(qtdDiasPrazoRegra){
//   const diasDaSemana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado'];  
//   var dataAprovacaoADM = new Date();//retorna: Sat Aug 26 2023 15:41:41 GMT-0300
//   var dataMaximoPagamento;  
//   console.log("Data de aprovação : " + formatarDataBrasil(dataAprovacaoADM));  
  
//   var contador = 1;
//     while(contador <= qtdDiasPrazoRegra){
  
//       if(contador != 1){
//         dataAprovacaoADM.setDate(dataAprovacaoADM.getDate() + 1);  
//       }
  
//       var diaData = parseInt(dataAprovacaoADM.getDay());  
  
//       if(diaData === 1 || diaData === 2 || diaData === 3 || diaData === 4 || diaData === 5){       
//         dataMaximoPagamento = dataAprovacaoADM;
//         console.log("Iteração n°" + contador + " " + formatarDataBrasil(dataMaximoPagamento) + " - Dia da semana: " + dataMaximoPagamento.getDay() + " " + diasDaSemana[dataMaximoPagamento.getDay()]);
//         contador++
//       }
//     }
//     return dataMaximoPagamento;
//   }
  
//   function formatarDataBrasil(dataCampo){
//       let data = new Date(dataCampo),
//           dia  = data.getDate().toString(),
//           diaF = (dia.length == 1) ? '0'+dia : dia,
//           mes  = (data.getMonth()+1).toString(),
//           mesF = (mes.length == 1) ? '0'+mes : mes,
//           anoF = data.getFullYear();
      
//       return diaF+"/"+mesF+"/"+anoF;
  
//   }
  
//   function formatarDataAmericano(dataCampo){
//       let data = new Date(dataCampo),
//           dia  = data.getDate().toString(),
//           diaF = (dia.length == 1) ? '0'+dia : dia,
//           mes  = (data.getMonth()+1).toString(),
//           mesF = (mes.length == 1) ? '0'+mes : mes,
//           anoF = data.getFullYear();
      
//       return anoF+"/"+mesF+"/"+diaF;
  
//   }
  
//   function calculo(dataAprv, dataVen){
//     dataAprv = moment(dataAprv); 
//     dataVen =  moment(dataVen);
//     const diferenca = moment.duration(dataVen.diff(dataAprv));
  
//     //Mostra a diferença em dias
//     const qtdDias = diferenca.asDays();
//     return qtdDias;
  
//   }
  