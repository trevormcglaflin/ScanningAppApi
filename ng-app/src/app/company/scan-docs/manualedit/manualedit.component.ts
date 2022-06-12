import { Component, OnInit, Input } from '@angular/core';
import { DocumentScanService } from '@/_services';

@Component({
  selector: 'app-manualedit',
  templateUrl: './manualedit.component.html',
  styleUrls: ['./manualedit.component.scss']
})
export class ManualeditComponent implements OnInit {
  @Input() companyId:any;
  @Input() documentId:any;
  incomeStatement:any = {};
  incomeStatementForm:any = {}

  constructor(private documentScanService: DocumentScanService) { }

  ngOnInit() {
    this.documentScanService.getIncomeStatementTemplate(this.companyId, this.documentId).subscribe(
      (res) => this.incomeStatementForm = res,
      (err) => console.log()
    );
    this.documentScanService.getIncomeStatementTemplate(this.companyId, this.documentId).subscribe(
      (res) => this.incomeStatement = res,
      (err) => console.log()
    );
  }

  onClickSubmit(data) {
    console.log(data.sales);
    var val = {
      year:data.year,
      sales:data.sales,
      returns_and_allowances:data.returns_and_allowance,
      net_sales:data.net_sales,
      cogs:data.cogs,
      gross_profit:data.gross_profit,
      total_operating_expense:data.total_operating_expense,
      salaries_and_wages_expense:data.salaries_and_wages_expense,
      repairs_and_maintenence_expense:data.repairs_and_maintenence_expense,
      bad_debt_expense:data.bad_debt_expense,
      rent_expense:data.rent_expense,
      taxes_and_licenses_expense:data.taxes_and_licenses_expense,
      interest_expense:data.interest_expense,
      charitable_contributions_expense:data.charitable_contributions_expense,
      depreciation_expense:data.depreciation_expense,
      depletion_expense:data.depletion_expense,
      advertising_expense:data.advertising_expense,
      operating_profit:data.operating_profit,
      other_income:data.other_income,
      taxable_income:data.taxable_income,
      income_tax_expense:data.income_tax_expense,
      net_income:data.net_income
    };
    this.documentScanService.addIncomeStatement(val, this.companyId).subscribe(res=>{
      alert("Are you sure?");
    });
 }
}
