from fineract.objects.currency import Currency
from fineract.objects.fineract_object import DataFineractObject, FineractObject
from fineract.objects.types import LoanType, TermPeriodFrequencyType


class Loan(DataFineractObject):
    """
    This class represents a Client.
    """

    def __repr__(self):
        return self.get__repr__({'loan_id': self.id})

    def _init_attributes(self):
        self.id = None
        self.account_no = None
        self.status = None
        self.client_id = None
        self.loan_product_id = None
        self.loan_purpose_id = None
        self.loan_purpose_name = None
        self.loan_type = None
        self.currency = None
        self.principal = None
        self.term_frequency = None
        self.term_frequency_type = None
        self.timeline = None
        self.summary = None
        self.multi_disburse_loan = None
        self.can_define_installment_amount = None
        self.can_disburse = None
        self.can_use_for_topup = None
        self.is_topup = None
        self.in_arrears = None
        self.is_npa = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.account_no = attributes.get('accountNo', None)
        self.status = self._make_fineract_object(LoanStatus, attributes.get('status', None))
        self.client_id = attributes.get('clientId', None)
        self.loan_product_id = attributes.get('loanProductId', None)
        self.loan_purpose_id = attributes.get('loanPurposeId', None)
        self.loan_purpose_name = attributes.get('loanPurposeName', None)
        self.loan_type = self._make_fineract_object(LoanType, attributes.get('loanType', None))
        self.currency = self._make_fineract_object(Currency, attributes.get('currency', None))
        self.principal = attributes.get('principal', None)
        self.term_frequency = attributes.get('termFrequency', None)
        self.term_frequency_type = self._make_fineract_object(TermPeriodFrequencyType,
                                                              attributes.get('termPeriodFrequencyType', None))
        self.timeline = self._make_fineract_object(LoanTimeline, attributes.get('timeline', None))
        self.summary = self._make_fineract_object(LoanSummary, attributes.get('summary', None))
        self.multi_disburse_loan = attributes.get('multiDisburseLoan', None)
        self.can_define_installment_amount = attributes.get('canDefineInstallmentAmount', None)
        self.can_disburse = attributes.get('canDisburse', None)
        self.can_use_for_topup = attributes.get('canUseForTopup', None)
        self.is_topup = attributes.get('isTopup', None)
        self.in_arrears = attributes.get('inArrears', None)
        self.is_npa = attributes.get('isNPA', None)


class LoanStatus(FineractObject):

    def _init_attributes(self):
        self.id = None
        self.code = None
        self.value = None
        self.pending_approval = None
        self.waiting_for_disbursal = None
        self.active = None
        self.closed_obligations_met = None
        self.close_written_off = None
        self.written_off = None
        self.closed_rescheduled = None
        self.closed = None
        self.overpaid = None

    def _use_attributes(self, attributes):
        self.id = attributes.get('id', None)
        self.code = attributes.get('code', None)
        self.value = attributes.get('value', None)
        self.pending_approval = attributes.get('pendingApproval', None)
        self.waiting_for_disbursal = attributes.get('waitingForDisbursal', None)
        self.active = attributes.get('active', None)
        self.closed_obligations_met = attributes.get('closedObligationsMet', None)
        self.close_written_off = attributes.get('closedWrittenOff', None)
        self.closed_rescheduled = attributes.get('closedRescheduled', None)
        self.closed = attributes.get('closed', None)
        self.overpaid = attributes.get('overpaid', None)


class LoanTimeline(FineractObject):
    """
    This class represent the timeline of a Loan
    """

    def _init_attributes(self):
        self.submitted_on = None
        self.submitted_by = None
        self.approved_on = None
        self.approved_by = None
        self.expected_disbursement_date = None
        self.actual_disbursement_date = None
        self.disbursed_by = None
        self.expected_maturity_date = None

    def _use_attributes(self, attributes):
        self.submitted_on = self._make_date_object(attributes.get('submittedOnDate', None))
        self.submitted_by = attributes.get('submittedByUsername', None)
        self.approved_on = self._make_date_object(attributes.get('approvedOnDate', None))
        self.approved_by = attributes.get('approvedByUsername', None)
        self.expected_disbursement_date = self._make_date_object(attributes.get('expectedDisbursementDate', None))
        self.actual_disbursement_date = self._make_date_object(attributes.get('actualDisbursementDate', None))
        self.disbursed_by = attributes.get('disbursedByUsername', None)
        self.expected_maturity_date = self._make_date_object(attributes.get('expectedMaturityDate', None))


class LoanSummary(FineractObject):
    """
    This is the summary of a Loan
    """

    def _init_attributes(self):
        self.principal_disbursed = None
        self.principal_paid = None
        self.principal_written_off = None
        self.principal_outstanding = None
        self.principal_overdue = None
        self.interest_charged = None
        self.interest_paid = None
        self.interest_waived = None
        self.interest_written_off = None
        self.interest_outstanding = None
        self.interest_overdue = None
        self.fee_charges_charged = None
        self.fee_charges_due_at_disbursement = None
        self.fee_charges_paid = None
        self.fee_charges_waived = None
        self.fee_charges_written_off = None
        self.fee_charges_outstanding = None
        self.fee_charges_overdue = None
        self.penalty_charges_charged = None
        self.penalty_charges_paid = None
        self.penalty_charges_waived = None
        self.penalty_charges_written_off = None
        self.penalty_charges_outstanding = None
        self.penalty_charges_overdue = None
        self.total_expected_repayment = None
        self.total_repayment = None
        self.total_expected_cost_of_loan = None
        self.total_cost_of_loan = None
        self.total_waived = None
        self.total_written_off = None
        self.outstanding = None
        self.overdue_since_date = None
        self.in_arrears = None
        self.is_npa = None

    def _use_attributes(self, attributes):
        self.principal_disbursed = attributes.get('principalDisbursed', None)
        self.principal_paid = attributes.get('principalPaid', None)
        self.principal_written_off = attributes.get('principalWrittenOff', None)
        self.principal_outstanding = attributes.get('principalOutstanding', None)
        self.principal_overdue = attributes.get('principalOverdue', None)
        self.interest_charged = attributes.get('interestCharged', None)
        self.interest_paid = attributes.get('interestPaid', None)
        self.interest_waived = attributes.get('interestWaived', None)
        self.interest_written_off = attributes.get('interestWrittenOff', None)
        self.interest_outstanding = attributes.get('interestOutstanding', None)
        self.interest_overdue = attributes.get('interestOverdue', None)
        self.fee_charges_charged = attributes.get('feeChargesCharged', None)
        self.fee_charges_due_at_disbursement = attributes.get('feeChargesDueAtDisbursementCharged', None)
        self.fee_charges_paid = attributes.get('feeChargesPaid', None)
        self.fee_charges_waived = attributes.get('feeChargesWaived', None)
        self.fee_charges_written_off = attributes.get('feeChargesWrittenOff', None)
        self.fee_charges_outstanding = attributes.get('feeChargesOutstanding', None)
        self.fee_charges_overdue = attributes.get('feeChargesOverdue', None)
        self.penalty_charges_charged = attributes.get('penaltyChargesCharged', None)
        self.penalty_charges_paid = attributes.get('penaltyChargesPaid', None)
        self.penalty_charges_waived = attributes.get('penaltyChargesWaived', None)
        self.penalty_charges_written_off = attributes.get('penaltyChargesWrittenOff', None)
        self.penalty_charges_outstanding = attributes.get('penaltyChargesOutstanding', None)
        self.penalty_charges_overdue = attributes.get('penaltyChargesOverdue', None)
        self.principal_disbursed = attributes.get('totalExpectedRepayment', None)
        self.principal_disbursed = attributes.get('totalRepayment', None)
        self.principal_disbursed = attributes.get('totalExpectedCostOfLoan', None)
        self.principal_disbursed = attributes.get('totalCostOfLoan', None)
        self.principal_disbursed = attributes.get('totalWaived', None)
        self.principal_disbursed = attributes.get('totalWrittenOff', None)
        self.principal_disbursed = attributes.get('totalOutstanding', None)
        self.principal_disbursed = attributes.get('totalOverdue', None)
        self.principal_disbursed = self._make_date_object(attributes.get('overdueSinceDate', None))
        self.in_arrears = attributes.get('inArrears', None)
        self.is_npa = attributes.get('isNPA', None)