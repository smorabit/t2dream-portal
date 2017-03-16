import pytest


@pytest.fixture
def file_exp(lab, award, testapp, experiment):
    item = {
        'lab': lab['uuid'],
        'award': award['uuid'],
        'assay_term_name': 'RAMPAGE',
        'biosample_term_id': 'NTR:000012',
        'biosample_term_name': 'Some body part',
        'possible_controls': [experiment['uuid']],
        'status': 'released',
        'date_released': '2016-01-01'
        }
    return testapp.post_json('/experiment', item, status=201).json['@graph'][0]


@pytest.fixture
def file_rep(replicate, file_exp, testapp):
    item = {
        'experiment': file_exp['uuid'],
        'biological_replicate_number': 1,
        'technical_replicate_number': 1
        }
    return testapp.post_json('/replicate', item, status=201).json['@graph'][0]


@pytest.fixture
def file_exp2(lab, award, testapp):
    item = {
        'lab': lab['uuid'],
        'award': award['uuid'],
        'assay_term_name': 'RAMPAGE',
        'biosample_term_id': 'NTR:000013',
        'biosample_term_name': 'Some other body part',
        'status': 'released',
        'date_released': '2016-01-01'
        }
    return testapp.post_json('/experiment', item, status=201).json['@graph'][0]


@pytest.fixture
def file_rep2(replicate, file_exp2, testapp):
    item = {
        'experiment': file_exp2['uuid'],
        'biological_replicate_number': 1,
        'technical_replicate_number': 1
        }
    return testapp.post_json('/replicate', item, status=201).json['@graph'][0]


@pytest.fixture
def file_rep1_2(replicate, file_exp, testapp):
    item = {
        'experiment': file_exp['uuid'],
        'biological_replicate_number': 2,
        'technical_replicate_number': 1
        }
    return testapp.post_json('/replicate', item, status=201).json['@graph'][0]


@pytest.fixture
def file1_2(file_exp, award, lab, file_rep1_2, testapp):
    item = {
        'dataset': file_exp['uuid'],
        'replicate': file_rep1_2['uuid'],
        'file_format': 'fastq',
        'md5sum': '91be74b6e11515393507f4ebfa66d58a',
        'output_type': 'raw data',
        'file_size': 34,
        'run_type': 'single-ended',
        'award': award['uuid'],
        'lab': lab['uuid'],
        'status': 'released'
    }
    return testapp.post_json('/file', item, status=201).json['@graph'][0]


@pytest.fixture
def file2(file_exp2, award, lab, file_rep2, platform1, testapp):
    item = {
        'dataset': file_exp2['uuid'],
        'replicate': file_rep2['uuid'],
        'file_format': 'fastq',
        'md5sum': '91be74b6e11515393507f4ebfa66d58b',
        'output_type': 'raw data',
        'file_size': 34,
        'run_type': 'single-ended',
        'platform': platform1['uuid'],
        'award': award['uuid'],
        'lab': lab['uuid'],
        'status': 'released'
    }
    return testapp.post_json('/file', item, status=201).json['@graph'][0]


@pytest.fixture
def file1(file_exp, award, lab, file_rep, file2, platform1, testapp):
    item = {
        'dataset': file_exp['uuid'],
        'replicate': file_rep['uuid'],
        'file_format': 'fastq',
        'md5sum': '91be74b6e11515393507f4ebfa66d58c',
        'output_type': 'reads',
        'file_size': 34,
        'run_type': 'single-ended',
        'platform': platform1['uuid'],
        'award': award['uuid'],
        'lab': lab['uuid'],
        'status': 'released',
        'controlled_by': [file2['uuid']]
    }
    return testapp.post_json('/file', item, status=201).json['@graph'][0]


@pytest.fixture
def file3(file_exp, award, lab, file_rep, testapp):
    item = {
        'dataset': file_exp['uuid'],
        'replicate': file_rep['uuid'],
        'file_format': 'fastq',
        'file_size': 34,
        'md5sum': '91be74b6e11515393507f4ebfa56d78d',
        'output_type': 'reads',
        'run_type': 'single-ended',
        'award': award['uuid'],
        'lab': lab['uuid'],
        'status': 'released'
    }
    return testapp.post_json('/file', item, status=201).json['@graph'][0]


@pytest.fixture
def file4(file_exp2, award, lab, file_rep2, testapp):
    item = {
        'dataset': file_exp2['uuid'],
        'replicate': file_rep2['uuid'],
        'file_format': 'fastq',
        'md5sum': '91ae74b6e11515393507f4ebfa66d78a',
        'output_type': 'reads',
        'file_size': 34,
        'run_type': 'single-ended',
        'award': award['uuid'],
        'lab': lab['uuid'],
        'status': 'released'
    }
    return testapp.post_json('/file', item, status=201).json['@graph'][0]


@pytest.fixture
def file6(file_exp2, award, encode_lab, testapp, analysis_step_run_bam):
    item = {
        'dataset': file_exp2['uuid'],
        'file_format': 'bam',
        'file_size': 3,
        'md5sum': '91ce74b6e11515393507f4ebfa66d78a',
        'output_type': 'alignments',
        'award': award['uuid'],
        'file_size': 34,
        'assembly': 'hg19',
        'lab': encode_lab['uuid'],
        'status': 'released',
        'step_run': analysis_step_run_bam['uuid']
    }
    return testapp.post_json('/file', item, status=201).json['@graph'][0]


@pytest.fixture
def file7(file_exp2, award, encode_lab, testapp, analysis_step_run_bam):
    item = {
        'dataset': file_exp2['uuid'],
        'file_format': 'tsv',
        'file_size': 3,
        'md5sum': '91be74b6e11515394507f4ebfa66d78a',
        'output_type': 'gene quantifications',
        'award': award['uuid'],
        'lab': encode_lab['uuid'],
        'status': 'released',
        'step_run': analysis_step_run_bam['uuid']
    }
    return testapp.post_json('/file', item, status=201).json['@graph'][0]


@pytest.fixture
def chipseq_bam_quality_metric(testapp, analysis_step_run_bam, file6, lab, award):
    item = {
        'step_run': analysis_step_run_bam['@id'],
        'award': award['@id'],
        'lab': lab['@id'],
        'quality_metric_of': [file6['@id']],
        'total': 20000000
    }

    return testapp.post_json('/samtools_flagstats_quality_metric', item).json['@graph'][0]


@pytest.fixture
def chipseq_bam_quality_metric_2(testapp, analysis_step_run_bam, file7, lab, award):
    item = {
        'step_run': analysis_step_run_bam['@id'],
        'award': award['@id'],
        'lab': lab['@id'],
        'quality_metric_of': [file7['@id']],
        'total': 20000000
    }

    return testapp.post_json('/samtools_flagstats_quality_metric', item).json['@graph'][0]


@pytest.fixture
def analysis_step_bam(testapp):
    item = {
        'name': 'bamqc',
        'title': 'bamqc',
        'input_file_types': ['reads'],
        'analysis_step_types': ['QA calculation']
    }
    return testapp.post_json('/analysis_step', item).json['@graph'][0]


@pytest.fixture
def pipeline_short_rna(testapp, lab, award, analysis_step_bam):
    item = {
        'award': award['uuid'],
        'lab': lab['uuid'],
        'title': "Small RNA-seq single-end pipeline",
        'analysis_steps': [analysis_step_bam['@id']]
    }
    return testapp.post_json('/pipeline', item).json['@graph'][0]


def test_audit_file_paired_with(testapp, file1):
    testapp.patch_json(file1['@id'], {'paired_end': '1'})
    res = testapp.get(file1['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'missing paired_with' for error in errors_list)


def test_audit_file_mismatched_paired_with(testapp, file1, file4):
    testapp.patch_json(file1['@id'], {'paired_end': '2', 'paired_with': file4['uuid']})
    res = testapp.get(file1['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'inconsistent paired_with' for error in errors_list)


def test_audit_read_length(testapp, file1):
    res = testapp.get(file1['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'missing read_length' for error in errors_list)


def test_audit_read_length_zero(testapp, file1):
    testapp.patch_json(file1['@id'], {'read_length': 0})
    res = testapp.get(file1['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'missing read_length' for error in errors_list)


def test_audit_file_missing_controlled_by(testapp, file3):
    res = testapp.get(file3['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'missing controlled_by' for error in errors_list)


def test_audit_file_mismatched_controlled_by(testapp, file1):
    res = testapp.get(file1['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'inconsistent control' for error in errors_list)


def test_audit_file_read_length_controlled_by(testapp, file1_2,
                                              file2, file_exp,
                                              file_exp2):
    testapp.patch_json(file1_2['@id'], {'read_length': 50,
                                        'run_type': 'single-ended'})
    testapp.patch_json(file2['@id'], {'read_length': 150,
                                      'run_type': 'single-ended'})
    testapp.patch_json(file1_2['@id'], {'controlled_by': [file2['@id']]})
    testapp.patch_json(file_exp['@id'], {'possible_controls': [file_exp2['@id']]})
    testapp.patch_json(file_exp2['@id'], {'assay_term_name': 'RAMPAGE',
                                          'biosample_term_id': 'NTR:000012',
                                          'biosample_term_name': 'Some body part'})
    res = testapp.get(file1_2['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'inconsistent control read length' for error in errors_list)


def test_audit_file_read_length_controlled_by_exclusion(testapp, file1_2,
                                                        file2, file_exp,
                                                        file_exp2):
    testapp.patch_json(file1_2['@id'], {'read_length': 50,
                                        'run_type': 'single-ended'})
    testapp.patch_json(file2['@id'], {'read_length': 52,
                                      'run_type': 'single-ended'})
    testapp.patch_json(file1_2['@id'], {'controlled_by': [file2['@id']]})
    testapp.patch_json(file_exp['@id'], {'possible_controls': [file_exp2['@id']]})
    testapp.patch_json(file_exp2['@id'], {'assay_term_name': 'RAMPAGE',
                                          'biosample_term_id': 'NTR:000012',
                                          'biosample_term_name': 'Some body part'})
    res = testapp.get(file1_2['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] != 'inconsistent control read length' for error in errors_list)


def test_audit_file_inconsistent_controlled_by(testapp, file1,
                                               file2, file3,
                                               file_rep1_2,
                                               file_rep2):
    testapp.patch_json(file1['@id'], {'replicate': file_rep2['@id']})
    testapp.patch_json(file3['@id'], {'replicate': file_rep1_2['@id']})
    testapp.patch_json(file1['@id'], {'controlled_by': [file2['@id'], file3['@id']]})

    res = testapp.get(file1['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'inconsistent controlled_by replicates' for
                                    error in errors_list)


def test_audit_file_missing_paired_controlled_by(testapp, file1,
                                                 file2, file3,
                                                 file_rep2):
    testapp.patch_json(file3['@id'], {'replicate': file_rep2['@id'],
                                      'paired_with': file2['@id'],
                                      'run_type': 'paired-ended',
                                      'paired_end': '2'})
    testapp.patch_json(file2['@id'], {'replicate': file_rep2['@id'],
                                      'run_type': 'paired-ended',
                                      'paired_end': '1'})
    testapp.patch_json(file1['@id'], {'controlled_by': [file2['@id']]})

    res = testapp.get(file1['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'missing paired_with in controlled_by' for
                                    error in errors_list)


def test_audit_file_replicate_match(testapp, file1, file_rep2):
    testapp.patch_json(file1['@id'], {'replicate': file_rep2['uuid']})
    res = testapp.get(file1['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'inconsistent replicate' for error in errors_list)


def test_audit_file_paired_ended_run_type1(testapp, file2, file_rep2):
    testapp.patch_json(file2['@id'] + '?validate=false', {'run_type': 'paired-ended',
                                                          'output_type': 'reads',
                                                          'file_size': 23498234})
    res = testapp.get(file2['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'missing paired_end' for error in errors_list)


def test_audit_file_paired_ended_run_type2(testapp, file2, file_rep2):
    testapp.patch_json(file2['@id'] + '?validate=false', {'run_type': 'paired-ended',
                                                          'output_type': 'reads',
                                                          'file_size': 23498234,
                                                          'paired_end': 1})
    res = testapp.get(file2['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'missing paired_with' for error in errors_list)


def test_audit_file_pipeline_status(testapp, file7, pipeline_bam):
    testapp.patch_json(file7['@id'], {'status': 'released'})
    res = testapp.get(file7['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'inconsistent pipeline status' for error in errors_list)


def test_audit_file_insufficient_control_read_depth_chip_seq_paired_end(
    testapp,
    file_exp,
    file_exp2,
    file6,
    file2,
    file7,
    file4,
    chipseq_bam_quality_metric,
    chipseq_bam_quality_metric_2,
    analysis_step_run_bam,
    analysis_step_version_bam,
    analysis_step_bam,
    target_H3K27ac,
    target_control,
        pipeline_bam):
    testapp.patch_json(file_exp['@id'], {'target': target_H3K27ac['@id']})
    testapp.patch_json(file_exp2['@id'], {'target': target_control['@id']})
    testapp.patch_json(chipseq_bam_quality_metric['@id'], {'total': 1000})
    testapp.patch_json(chipseq_bam_quality_metric_2['@id'], {'total': 1000})
    testapp.patch_json(file2['@id'], {'dataset': file_exp2['@id']})
    testapp.patch_json(file7['@id'], {'dataset': file_exp2['@id'],
                                      'file_format': 'bam',
                                      'output_type': 'alignments',
                                      'assembly': 'hg19',
                                      'derived_from': [file2['@id']]})

    testapp.patch_json(file4['@id'], {'dataset': file_exp['@id'],
                                      'controlled_by': [file2['@id']]})
    testapp.patch_json(file6['@id'], {'dataset': file_exp['@id'],
                                      'assembly': 'hg19',
                                      'derived_from': [file4['@id']]})
    testapp.patch_json(file4['@id'], {'run_type': 'paired-ended'})
    testapp.patch_json(file2['@id'], {'run_type': 'paired-ended'})
    testapp.patch_json(file7['@id'], {})
    res = testapp.get(file6['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'control extremely low read depth' for error in errors_list)


def test_audit_modERN_missing_step_run(testapp, file_exp, file3, award):
    testapp.patch_json(award['@id'], {'rfa': 'modERN'})
    testapp.patch_json(file_exp['@id'], {'assay_term_name': 'ChIP-seq'})
    testapp.patch_json(file3['@id'], {'dataset': file_exp['@id'], 'file_format': 'bam',
                                      'assembly': 'ce10', 'output_type': 'alignments'})
    res = testapp.get(file3['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'missing step_run' for error in errors_list)


def test_audit_modERN_missing_derived_from(testapp, file_exp, file3, award, analysis_step_version_bam, analysis_step_bam, analysis_step_run_bam):
    testapp.patch_json(award['@id'], {'rfa': 'modERN'})
    testapp.patch_json(file_exp['@id'], {'assay_term_name': 'ChIP-seq'})
    testapp.patch_json(file3['@id'], {'dataset': file_exp['@id'], 'file_format': 'bam', 'assembly': 'ce10',
                                      'output_type': 'alignments', 'step_run': analysis_step_run_bam['@id']})
    res = testapp.get(file3['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'missing derived_from' for error in errors_list)


def test_audit_modERN_wrong_step_run(testapp, file_exp, file3, file4, award, analysis_step_version_bam, analysis_step_bam, analysis_step_run_bam):
    testapp.patch_json(award['@id'], {'rfa': 'modERN'})
    testapp.patch_json(file_exp['@id'], {'assay_term_name': 'ChIP-seq'})
    testapp.patch_json(file3['@id'], {'dataset': file_exp['@id'], 'file_format': 'bed',
                                      'file_format_type': 'narrowPeak', 'output_type': 'peaks',
                                      'step_run': analysis_step_run_bam['@id'], 'assembly': 'ce11',
                                      'derived_from': [file4['@id']]})
    res = testapp.get(file3['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'wrong step_run for peaks' for error in errors_list)


def test_audit_modERN_unexpected_step_run(testapp, file_exp, file2, award, analysis_step_run_bam):
    testapp.patch_json(award['@id'], {'rfa': 'modERN'})
    testapp.patch_json(file_exp['@id'], {'assay_term_name': 'ChIP-seq'})
    testapp.patch_json(file2['@id'], {'dataset': file_exp['@id'], 'step_run': analysis_step_run_bam['@id']})
    res = testapp.get(file2['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'unexpected step_run' for error in errors_list)


def test_audit_file_biological_replicate_number_match(testapp,
                                                      file_exp,
                                                      file_rep,
                                                      file1,
                                                      file_rep1_2,
                                                      file1_2):
    testapp.patch_json(file1['@id'], {'derived_from': [file1['@id']]})
    res = testapp.get(file1['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert all(error['category'] != 'inconsistent replicate'
               for error in errors_list)


def test_audit_file_biological_replicate_number_mismatch(testapp,
                                                         file_exp,
                                                         file_rep,
                                                         file1,
                                                         file_rep1_2,
                                                         file1_2):
    testapp.patch_json(file1['@id'], {'derived_from': [file1_2['@id']]})
    res = testapp.get(file1['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'inconsistent replicate'
               for error in errors_list)


def test_audit_file_fasta_assembly(testapp, file4):
    testapp.patch_json(file4['@id'], {'file_format': 'fasta', 'output_type': 'raw data',
                                      'assembly': 'GRCh38'})
    res = testapp.get(file4['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'unexpected property'
               for error in errors_list)


def test_audit_file_rbns_assembly(testapp, file4, file_exp):
    testapp.patch_json(file_exp['@id'], {'assay_term_name': 'RNA Bind-n-Seq'})
    testapp.patch_json(file4['@id'], {'assembly': 'GRCh38',
                                      'dataset': file_exp['@id'],
                                      'file_format': 'bam',
                                      'output_type': 'alignments'})
    res = testapp.get(file4['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'unexpected property'
               for error in errors_list)


def test_audit_file_assembly(testapp, file6, file7):
    testapp.patch_json(file6['@id'], {'assembly': 'GRCh38'})
    testapp.patch_json(file7['@id'], {'derived_from': [file6['@id']],
                                      'assembly': 'hg19'})
    res = testapp.get(file7['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'inconsistent assembly'
               for error in errors_list)


def test_audit_file_missing_assembly_no_derived(testapp, file7):
    res = testapp.get(file7['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'missing assembly'
               for error in errors_list)


def test_audit_file_missing_assembly(testapp, file6, file7):
    testapp.patch_json(file6['@id'], {'assembly': 'GRCh38'})
    testapp.patch_json(file7['@id'], {'derived_from': [file6['@id']]})
    res = testapp.get(file7['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'missing assembly'
               for error in errors_list)


def test_audit_file_derived_from_revoked(testapp, file6, file7):
    testapp.patch_json(file6['@id'], {'assembly': 'hg19', 'status': 'revoked'})
    testapp.patch_json(file7['@id'], {'derived_from': [file6['@id']],
                                      'status': 'released'})
    res = testapp.get(file7['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'mismatched file status'
               for error in errors_list)


def test_audit_file_derived_from_empty(testapp, file7):
    res = testapp.get(file7['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'missing derived_from'
               for error in errors_list)


def test_audit_file_bam_derived_from_no_fastq(testapp, file7, file6):
    testapp.patch_json(file6['@id'], {'derived_from': [file7['@id']],
                                      'status': 'released',
                                      'file_format': 'bam',
                                      'assembly': 'hg19'})
    testapp.patch_json(file7['@id'], {'file_format': 'tsv', 'assembly': 'hg19'})
    res = testapp.get(file6['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'missing derived_from'
               for error in errors_list)


def test_audit_file_bam_derived_from_bam_no_fastq(testapp, file7, file6):
    testapp.patch_json(file6['@id'], {'derived_from': [file7['@id']],
                                      'status': 'released',
                                      'file_format': 'bam',
                                      'assembly': 'hg19'})
    testapp.patch_json(file7['@id'], {'file_format': 'bam', 'assembly': 'hg19'})
    res = testapp.get(file6['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert all(error['category'] != 'missing derived_from'
               for error in errors_list)


def test_audit_file_bam_derived_from_different_experiment(testapp, file6, file4, file_exp):
    testapp.patch_json(file4['@id'], {'dataset': file_exp['@id']})
    testapp.patch_json(file6['@id'], {'derived_from': [file4['@id']],
                                      'assembly': 'hg19',
                                      'status': 'released'})
    res = testapp.get(file6['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'inconsistent derived_from'
               for error in errors_list)

'''
def test_audit_file_md5sum(testapp, file1):
    testapp.patch_json(file1['@id'], {'md5sum': 'some_random_text'})
    res = testapp.get(file1['@id'] + '@@index-data')
    errors = res.json['audit']
    errors_list = []
    for error_type in errors:
        errors_list.extend(errors[error_type])
    assert any(error['category'] == 'inconsistent md5sum'
               for error in errors_list)
'''