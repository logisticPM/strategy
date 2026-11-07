"""Reproduce disclosed arithmetic and explicitly hypothetical sensitivities, US$M."""
import json
from pathlib import Path


def calculate():
    prior = dict(revenue=2525.219, gross_profit=1477.202, sga=951.658, amortization=1.730, operating_income=523.814)
    current = dict(revenue=2415.631, gross_profit=1461.878, sga=1006.332, amortization=1.893, operating_income=453.653)
    for row in (prior, current):
        assert abs(row['gross_profit'] - row['sga'] - row['amortization'] - row['operating_income']) < 1e-8
    bridge = dict(gross_profit_change=current['gross_profit']-prior['gross_profit'],
                  sga_effect=prior['sga']-current['sga'],
                  amortization_effect=prior['amortization']-current['amortization'])
    delta = current['operating_income']-prior['operating_income']
    residual = delta-sum(bridge.values())
    assert abs(residual) < 1e-8
    refund = 134.5
    americas = 7847.044
    matrix = []
    for growth in (.005, .01, .02):
        for cm in (.2, .3, .4):
            incremental_revenue = americas*growth
            matrix.append(dict(assumed_recovery_fraction=growth, assumed_incremental_contribution_margin=cm,
                               incremental_net_revenue=round(incremental_revenue, 3), assumed_fixed_cost=10,
                               incremental_contribution_after_fixed_cost=round(incremental_revenue*cm-10, 3)))
    return dict(source_ids=['E012','E040'], units='US$ million',
                scope='Arithmetic checks, not causal validation or forecast; scenario inputs are invented sensitivities.',
                q2_prior=prior, q2_current=current,
                operating_income_bridge={k:round(v,3) for k,v in bridge.items()},
                operating_income_change=round(delta,3), bridge_residual=round(residual,8),
                excluding_only_current_tariff_refund=dict(
                    gross_profit=round(current['gross_profit']-refund,3),
                    operating_income=round(current['operating_income']-refund,3),
                    gross_margin=(current['gross_profit']-refund)/current['revenue'],
                    operating_margin=(current['operating_income']-refund)/current['revenue'],
                    warning='Not company adjusted metrics or full normalization; interest refund not in operating income.'),
                annual_regional_reported_revenue_changes=dict(Americas=-81.112, China=393.462, ROW=202.124, total=514.474),
                assumed_sensitivity_matrix=matrix,
                assumed_fixed_10m_break_even_revenue={str(cm):round(10/cm,3) for cm in (.2,.3,.4)},
                global_fy2025_100bps_profit_sensitivity=111.026,
                unresolved_inputs=['country cohort cash flows','incremental margins','cannibalization','capex','working capital','avoidable costs'])


if __name__ == '__main__':
    result = calculate()
    output = Path(__file__).with_name('enterprise-economics-results.json')
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'output':str(output), 'bridge_residual':result['bridge_residual'], 'scenario_cells':len(result['assumed_sensitivity_matrix'])}))
